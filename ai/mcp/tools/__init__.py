"""AI tool modules for Copilot-style agents.

Each module exposes a tool class that implements `BaseTool.run(prompt)`.
"""

from .aiml import AIMLTool
from .architecture_advisor import ArchitectureAdvisorTool
from .data_sql import DataSQLTool
from .debug import DebugTool
from .doc import DocTool
from .devops_cicd import DevOpsCICDTool
from .node_api import NodeApiTool
from .react_frontend import ReactFrontendTool
from .refactor import RefactorTool
from .test import TestTool
from .utdoc import UTDocTool
from .automation import PythonAutomationTool

# ✅ Export classes
__all__ = [
    "AIMLTool",
    "ArchitectureAdvisorTool",
    "DataSQLTool",
    "DebugTool",
    "DocTool",
    "DevOpsCICDTool",
    "NodeApiTool",
    "ReactFrontendTool",
    "RefactorTool",
    "TestTool",
    "UTDocTool",
    "PythonAutomationTool",
]

# ADD THIS → TOOL REGISTRY
TOOLS = {
    PythonAutomationTool.name: PythonAutomationTool(),
    AIMLTool.name: AIMLTool(),
    ArchitectureAdvisorTool.name: ArchitectureAdvisorTool(),
    DataSQLTool.name: DataSQLTool(),
    DebugTool.name: DebugTool(),
    DocTool.name: DocTool(),
    DevOpsCICDTool.name: DevOpsCICDTool(),
    NodeApiTool.name: NodeApiTool(),
    ReactFrontendTool.name: ReactFrontendTool(),
    RefactorTool.name: RefactorTool(),
    TestTool.name: TestTool(),
    UTDocTool.name: UTDocTool(),
}