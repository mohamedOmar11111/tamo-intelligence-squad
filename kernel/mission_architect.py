import os
import datetime
import uuid

class MissionArchitect:
    def __init__(self, project_root):
        self.project_root = project_root
        self.template_path = os.path.join(project_root, "assets", "report_template.html")
        self.reports_dir = os.path.join(project_root, "reports")
        os.makedirs(self.reports_dir, exist_ok=True)

    def generate_report(self, squad_name, target_domain, mission_output):
        with open(self.template_path, "r") as f:
            template = f.read()

        mission_id = str(uuid.uuid4())[:8].upper()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Basic markdown to HTML conversion for the output
        formatted_output = mission_output.replace("\n", "<br>").replace("###", "<h3>").replace("##", "<h2>")

        # Use manual replace to avoid KeyError from CSS curly braces
        report_content = template.replace("{mission_id}", mission_id)
        report_content = report_content.replace("{timestamp}", timestamp)
        report_content = report_content.replace("{squad_name}", squad_name)
        report_content = report_content.replace("{target_domain}", target_domain)
        report_content = report_content.replace("{mission_output}", formatted_output)

        report_filename = f"mission_{mission_id}.html"
        report_path = os.path.join(self.reports_dir, report_filename)

        with open(report_path, "w") as f:
            f.write(report_content)

        return report_path
