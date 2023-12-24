import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from model import OrbitalDataManager, AstronomyCalculator # 导入新的 Form 类
import csv

class mainUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Orbital Parameters Management System")

        # 实例化表单类
        self.parameter_form = OrbitalDataManager()  # 使用新的 Form 类
        self.astronomy_calculator = AstronomyCalculator(self.parameter_form)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # 创建一个容器来放置轨道参数的按钮和表格
        self.object_frame = tk.Frame(root)
        self.object_frame.grid(row=0, column=0)

        # 添加显示所有轨道参数的按钮
        self.show_all_parameters_button = tk.Button(self.object_frame, text="Show All Parameters", command=self.show_all_parameters)
        self.show_all_parameters_button.grid(row=0, column=0)

        # 添加添加空条目的按钮
        self.add_empty_parameter_button = tk.Button(self.object_frame, text="Add Empty Parameter", command=self.add_empty_parameter)
        self.add_empty_parameter_button.grid(row=0, column=1)

        # 添加删除选中条目的按钮
        self.delete_parameter_button = tk.Button(self.object_frame, text="Delete Selected Parameter", command=self.delete_selected_parameter)
        self.delete_parameter_button.grid(row=0, column=2)

        # 创建表格控件
        self.parameter_tree = ttk.Treeview(root, columns=("ID", "Name", "Data Format", "Line 1", "Line 2", "Line 3", "Description"), show='headings')
        self.parameter_tree.heading("ID", text="ID")
        self.parameter_tree.heading("Name", text="Name")
        self.parameter_tree.heading("Data Format", text="Data Format")
        self.parameter_tree.heading("Line 1", text="Line 1")
        self.parameter_tree.heading("Line 2", text="Line 2")
        self.parameter_tree.heading("Line 3", text="Line 3")
        self.parameter_tree.heading("Description", text="Description")
        self.parameter_tree.grid(row=1, column=0)

        # 为轨道参数表格添加可编辑的功能
        self.parameter_tree.bind("<Double-1>", self.on_parameter_click)  # 双击进行编辑
        self.parameter_entry_edit = tk.Entry(root, bd=0)
        self.parameter_entry_edit.place(x=-100, y=-100)
        self.parameter_entry_edit.bind("<Return>", self.save_parameter_edit)
        self.parameter_entry_edit.bind("<FocusOut>", self.save_parameter_edit)
 # 添加导出按钮
        self.export_button = tk.Button(self.object_frame, text="Export Data", command=self.on_export_click)
        self.export_button.grid(row=0, column=4)

        # 添加导入按钮
        self.import_button = tk.Button(self.object_frame, text="Import Data", command=self.on_import_click)
        self.import_button.grid(row=0, column=5)

        # 添加计算星座的按钮
        self.constellation_button = tk.Button(self.object_frame, text="Calculate Constellation", command=self.open_constellation_window)
        self.constellation_button.grid(row=1, column=0)

        # 添加计算星体位置的按钮
        self.position_button = tk.Button(self.object_frame, text="Calculate Position", command=self.open_position_window)
        self.position_button.grid(row=1, column=1)

    def open_position_window(self):
        # 创建新窗口
        self.position_window = tk.Toplevel(self.root)
        self.position_window.title("Star Position Calculator")

        # 创建输入字段和标签
        tk.Label(self.position_window, text="Star Name:").grid(row=0, column=0)
        self.star_name_entry_pos = tk.Entry(self.position_window)
        self.star_name_entry_pos.grid(row=0, column=1)

        tk.Label(self.position_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
        self.date_entry_pos = tk.Entry(self.position_window)
        self.date_entry_pos.grid(row=1, column=1)

        # 添加提交按钮
        submit_button = tk.Button(self.position_window, text="Submit", command=self.calculate_position)
        submit_button.grid(row=2, column=0, columnspan=2)

    def calculate_position(self):
        star_name = self.star_name_entry_pos.get()
        date_str = self.date_entry_pos.get()

        # 调用后端方法计算星体位置
        result = self.astronomy_calculator.calculate_position(star_name, date_str)

        # 显示结果
        messagebox.showinfo("Star Position", str(result))

        # 关闭新创建的窗口
        self.position_window.destroy()


    def open_constellation_window(self):
        # 创建新窗口
        self.constellation_window = tk.Toplevel(self.root)
        self.constellation_window.title("Constellation Calculator")

        # 创建输入字段和标签
        tk.Label(self.constellation_window, text="Star Name:").grid(row=0, column=0)
        self.star_name_entry = tk.Entry(self.constellation_window)
        self.star_name_entry.grid(row=0, column=1)

        tk.Label(self.constellation_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
        self.date_entry = tk.Entry(self.constellation_window)
        self.date_entry.grid(row=1, column=1)

        # 添加提交按钮
        submit_button = tk.Button(self.constellation_window, text="Submit", command=self.calculate_constellation)
        submit_button.grid(row=2, column=0, columnspan=2)

    def calculate_constellation(self):
        star_name = self.star_name_entry.get()
        date_str = self.date_entry.get()

        # 调用后端方法计算星座
        result = self.astronomy_calculator.calculate_constellation(star_name, date_str)

        # 格式化显示结果
        if isinstance(result, tuple) and len(result) == 2:
            constellation_name, (ra, dec) = result
            formatted_result = f"Star: {star_name}\nDate: {date_str}\n" \
                            f"Constellation: {constellation_name}\n" \
                            f"Right Ascension: {ra}\nDeclination: {dec}"
        else:
            formatted_result = result  # 当结果不是预期格式时，直接显示原始结果

        # 显示结果
        messagebox.showinfo("Constellation Result", formatted_result)

        # 关闭新创建的窗口
        self.constellation_window.destroy()


    def on_export_click(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.export_data_to_csv(file_path)

    def on_import_click(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.import_data_from_csv(file_path)

    def export_data_to_csv(self, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 写入列标题
            writer.writerow(["ID", "Name", "Data Format", "Line 1", "Line 2", "Line 3", "Description"])
            # 写入数据
            for param in self.parameter_form.get_all_parameters():
                writer.writerow([
                    param.get_id(), 
                    param.get_name(), 
                    param.get_data_format(), 
                    param.get_line_1(), 
                    param.get_line_2(), 
                    param.get_line_3(), 
                    param.get_description()
                ])
        messagebox.showinfo("Export", "Data exported successfully to " + file_path)

    def import_data_from_csv(self, file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # 跳过列标题
            for row in reader:
                if len(row) == 7:  # 确保行有正确的列数
                    self.parameter_form.add_parameter(
                        id=row[0], name=row[1], data_format=row[2],
                        line_1=row[3], line_2=row[4], line_3=row[5],
                        description=row[6]
                    )
        messagebox.showinfo("Import", "Data imported successfully from " + file_path)

    # 这里是添加、删除、显示、编辑和保存轨道参数的方法
    # 请根据 OrbitalParameter 类的方法来实现这些功能

    def add_empty_parameter(self):
        # 在表格中添加一条空记录
        self.parameter_tree.insert("", "end", values=("", "", "", "", "", "", ""))

        # 调用后端方法添加空记录
        self.parameter_form.add_parameter(0, "", "", "", "", "", "")  # 注意：这里可能需要修改以适应 add_parameter 方法的参数要求
        self.show_all_parameters()

    def delete_selected_parameter(self):
        selected_items = self.parameter_tree.selection()  # 获取选中的条目
        for item in selected_items:
            # 获取选中条目的 ID
            param_id = self.parameter_tree.item(item, 'values')[0]

            # 删除表格中的条目
            self.parameter_tree.delete(item)

            # 调用后端方法删除数据库中的条目
            self.parameter_form.remove_parameter_by_id(param_id)

    def show_all_parameters(self):
        # 清空表格中现有的行
        for i in self.parameter_tree.get_children():
            self.parameter_tree.delete(i)

        # 获取所有轨道参数
        parameters = self.parameter_form.get_all_parameters()

        # 将轨道参数添加到表格中
        for param in parameters:
            self.parameter_tree.insert("", "end", values=(
                param.get_id(), 
                param.get_name(), 
                param.get_data_format(), 
                param.get_line_1(), 
                param.get_line_2(), 
                param.get_line_3(), 
                param.get_description()
            ))

    def on_parameter_click(self, event):
        # 获取被点击的单元格的行列信息
        row_id = self.parameter_tree.identify_row(event.y)
        column_id = self.parameter_tree.identify_column(event.x)

        # 防止在表头上双击时出错
        if row_id == '':
            # 表头被点击，不执行任何操作
            return

        # 获取单元格的位置和大小
        x, y, width, height = self.parameter_tree.bbox(row_id, column_id)

        # 获取 Treeview 控件的绝对坐标
        tree_x = self.parameter_tree.winfo_x()
        tree_y = self.parameter_tree.winfo_y()

        # 显示输入框于相应位置
        self.parameter_entry_edit.place(x=x+tree_x, y=y+tree_y, width=width, height=height)

        # 设置输入框的当前值
        self.parameter_entry_edit.delete(0, tk.END)
        self.parameter_entry_edit.insert(0, self.parameter_tree.item(row_id, 'values')[int(column_id[1:]) - 1])
        self.parameter_entry_edit.focus()

        # 保存当前编辑的行和列信息
        self.current_parameter_item = row_id
        self.current_parameter_column = int(column_id[1:]) - 1


    def save_parameter_edit(self, event):
        # 获取输入框的值并更新到表格中
        new_value = self.parameter_entry_edit.get()
        current_values = list(self.parameter_tree.item(self.current_parameter_item, 'values'))
        current_values[self.current_parameter_column] = new_value
        self.parameter_tree.item(self.current_parameter_item, values=current_values)

        # 隐藏输入框
        self.parameter_entry_edit.place(x=-100, y=-100)

        # 更新后端数据
        self.update_parameter_backend_data(self.current_parameter_item, self.current_parameter_column, new_value)

    def update_parameter_backend_data(self, row_id, column_index, new_value):
        # 获取当前行的所有值
        values = self.parameter_tree.item(row_id, 'values')

        # 从当前行获取 ID
        param_id = values[0]  # 假设 ID 在第一列

        # 根据列索引更新相应的参数
        name = values[1] if column_index != 1 else new_value
        data_format = values[2] if column_index != 2 else new_value
        line_1 = values[3] if column_index != 3 else new_value
        line_2 = values[4] if column_index != 4 else new_value
        line_3 = values[5] if column_index != 5 else new_value
        description = values[6] if column_index != 6 else new_value

        # 调用 update_parameter_record 方法更新后端数据
        self.parameter_form.update_parameter_record(
            id=param_id, 
            name=name, 
            data_format=data_format,
            line_1=line_1,
            line_2=line_2,
            line_3=line_3,
            description=description
        )


# 创建 Tkinter 窗口并运行
root = tk.Tk()
app = mainUI(root)
root.mainloop()
