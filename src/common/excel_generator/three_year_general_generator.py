from common.excel_generator.abstract import AbstractGenerator


class OneThreeGeneralGenerator (AbstractGenerator):
    def do(self,workbook, worksheet):
        count = len(self.data[0])
        worksheet.write_column('A2', self.data[0])
        worksheet.write_column('B2', self.data[1])
        chart_col = workbook.add_chart({'type': 'column'})
        chart_col.add_series({
            # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
            # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
            'name': '=three_year!$B$1',
            'categories':   '=three_year!$B$2:$B$'+count,
            'values': '=three_year!$A$2:$A$'+count,
            'line': {'color': 'blue'},
        })
        chart_col.set_title({'name': '三年年年行业分析'})
        chart_col.set_x_axis({'name': '行业'})
        chart_col.set_y_axis({'name':  '涨幅'})
        chart_col.set_style(1)
        worksheet.insert_chart(
            'A110', chart_col, {'x_offset': 250, 'y_offset': 10})
        workbook.close()