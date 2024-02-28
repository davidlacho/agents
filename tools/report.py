from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel


def write_report(filename, html):
    with open(filename, "w") as f:
        f.write(html)


class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str


# "Tool" class can only receive one argument
# To receive multiple arguments, use "StructuredTool"
write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Write a nicely formatted and styled HTML file to disk. Use this tool whenever someone asks for a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema,
)
