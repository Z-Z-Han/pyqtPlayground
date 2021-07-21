from PyQt5.QtChart import QChartView, QChart, QPieSeries
from PyQt5.QtGui import QPainter, QColor


class PieWindow(QChartView):

    def __init__(self, *args, **kwargs):
        super(PieWindow, self).__init__(*args, **kwargs)
        self.resize(80, 40)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple piechart example')
        # 添加Series
        chart.addSeries(self.getSeries())

    def getSeries(self):
        series = QPieSeries()
        slice0 = series.append('10%', 1)
        series.append('20%', 2)
        series.append('70%', 7)
        # 显示label文字
        series.setLabelsVisible()
        series.setPieSize(0.5)
        # 使第一块突出显示
        slice0.setLabelVisible()
        slice0.setExploded()
        # 设置第一块颜色
        slice0.setColor(QColor(255, 0, 0, 100))
        return series
