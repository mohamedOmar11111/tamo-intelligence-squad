import sys
import os

# Link to Global Growth Engine System
sys.path.append("/Users/o-elkhazragy/Desktop/Growth_Architect_HQ/00_System/Shared_Brain")

try:
    from engine_memory import EngineMemory
except ImportError:
    # Fallback if running outside of HQ
    EngineMemory = object 

class TAMOMemory(EngineMemory):
    """The TAMO implementation of the Global Engine Memory."""
    def __init__(self):
        super().__init__()

    def record_fact(self, fact, user_id="growth_architect", metadata=None):
        self.capture_intelligence(fact, client="tamo_public", squad="recon", metadata=metadata)

    def retrieve_context(self, query, user_id="growth_architect"):
        return self.find_patterns(query)

