from .writer_interface import WriterInterface


class ReportFileWriter(WriterInterface):

    @staticmethod
    def write(report):
        file = open('report.txt', 'w')
        file.write(report)
        file.close()
