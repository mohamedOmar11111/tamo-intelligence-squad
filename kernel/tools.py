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
        # Check for common MCP environment variables or config paths
        mcp_paths = [
            os.path.expanduser("~/.mcp.json"),
            os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
        ]
        active_mcp = any(os.path.exists(path) for path in mcp_paths)
        return "MCP_LINK_ACTIVE" if active_mcp else "MCP_STANDALONE_MODE"
