from .file_writer import ReportFileWriter


class ReportWriter:

    @staticmethod
    def write(report, writer=ReportFileWriter):
        writer.write(report)
