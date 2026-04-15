import os
from exa_py import Exa
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

class TAMOTools:
    def __init__(self):
        self.exa_key = os.getenv("EXA_API_KEY")
        self.firecrawl_key = os.getenv("FIRECRAWL_API_KEY")
        
        # Initialize clients only if keys exist
        self.exa = Exa(api_key=self.exa_key) if self.exa_key else None
        self.firecrawl = FirecrawlApp(api_key=self.firecrawl_key) if self.firecrawl_key else None

    def exa_search(self, query, num_results=5):
        """Execute deep semantic search via Exa."""
        if not self.exa:
            return "ERROR: EXA_API_KEY not configured."
        
        results = self.exa.search(
            query,
            num_results=num_results,
            use_autoprompt=True
        )
        return results

    def firecrawl_scrape(self, url):
        """Forensic web scraping via Firecrawl."""
        if not self.firecrawl:
            return "ERROR: FIRECRAWL_API_KEY not configured."
        
        scrape_result = self.firecrawl.scrape_url(url, params={'formats': ['markdown']})
        return scrape_result

    def check_mcp_status(self):
        """Verification node for MCP compatibility."""
        mcp_paths = [
            os.path.expanduser("~/.mcp.json"),
            os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
        ]
        active_mcp = any(os.path.exists(path) for path in mcp_paths)
        return "MCP_LINK_ACTIVE" if active_mcp else "MCP_STANDALONE_MODE"

    def update_credentials(self, exa_key=None, firecrawl_key=None):
        """Surgically update the .env file with new credentials."""
        env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        
        lines = []
        if os.path.exists(env_path):
            with open(env_path, "r") as f:
                lines = f.readlines()

        new_lines = []
        found_exa = False
        found_fire = False

        for line in lines:
            if line.startswith("EXA_API_KEY=") and exa_key:
                new_lines.append(f"EXA_API_KEY={exa_key}\n")
                found_exa = True
            elif line.startswith("FIRECRAWL_API_KEY=") and firecrawl_key:
                new_lines.append(f"FIRECRAWL_API_KEY={firecrawl_key}\n")
                found_fire = True
            else:
                new_lines.append(line)

        if not found_exa and exa_key:
            new_lines.append(f"EXA_API_KEY={exa_key}\n")
        if not found_fire and firecrawl_key:
            new_lines.append(f"FIRECRAWL_API_KEY={firecrawl_key}\n")

        with open(env_path, "w") as f:
            f.writelines(new_lines)
        
        # Refresh local state
        load_dotenv(override=True)
        self.exa_key = os.getenv("EXA_API_KEY")
        self.firecrawl_key = os.getenv("FIRECRAWL_API_KEY")
        if self.exa_key: self.exa = Exa(api_key=self.exa_key)
        if self.firecrawl_key: self.firecrawl = FirecrawlApp(api_key=self.firecrawl_key)
        return True
