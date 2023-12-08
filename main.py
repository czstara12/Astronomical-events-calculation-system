import tkinter as tk
from tkinter import ttk
from model import AstronomicalEventForm, AstronomicalObservationForm, CelestialObjectForm
from tkinter import messagebox

class AstronomyManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Astronomical events calculation system")

        # 实例化表单类
        self.observation_form = AstronomicalObservationForm(root)
        self.event_form = AstronomicalEventForm()
        self.object_form = CelestialObjectForm()

        # 创建界面元素（按钮、文本框等）

        # 观测记录部分的容器和控件
        self.observation_frame = tk.Frame(root)
        self.observation_frame.pack()

        # 添加观测记录相关按钮
        self.btn_show_observations = tk.Button(self.observation_frame, text="Show All Observations", command=self.show_all_observations)
        self.btn_show_observations.grid(row=0, column=0)
        self.btn_add_empty_observation = tk.Button(self.observation_frame, text="Add Empty Observation", command=self.add_empty_observation)
        self.btn_add_empty_observation.grid(row=0, column=1)
        self.btn_delete_observation = tk.Button(self.observation_frame, text="Delete Selected Observation", command=self.delete_selected_observation)
        self.btn_delete_observation.grid(row=0, column=2)

        # 创建表格控件
        self.observation_tree = ttk.Treeview(root, columns=("ID", "Date", "Location", "Celestial Body", "Type", "Conditions", "Observer", "Notes"), show='headings')
        self.observation_tree.heading("ID", text="ID")
        self.observation_tree.heading("Date", text="Date")
        self.observation_tree.heading("Location", text="Location")
        self.observation_tree.heading("Celestial Body", text="Celestial Body")
        self.observation_tree.heading("Type", text="Type")
        self.observation_tree.heading("Conditions", text="Conditions")
        self.observation_tree.heading("Observer", text="Observer")
        self.observation_tree.heading("Notes", text="Notes")
        self.observation_tree.pack()
        #self.show_all_observations()

        # 为观测记录表格添加可编辑的功能
        self.observation_tree.bind("<Double-1>", self.on_observation_click)  # 双击进行编辑
        self.entry_observation_edit = tk.Entry(root, bd=0)
        self.entry_observation_edit.place(x=-100, y=-100)
        self.entry_observation_edit.bind("<Return>", self.save_observation_edit)
        
        # 创建一个容器来放置按钮和表格
        self.event_frame = tk.Frame(root)
        self.event_frame.pack()

        # 添加显示天文事件的按钮
        self.show_all_events_button = tk.Button(self.event_frame, text="Show All Events", command=self.show_all_events)
        self.show_all_events_button.grid(row=0, column=0)

        # 添加添加空条目的按钮
        self.add_empty_event_button = tk.Button(self.event_frame, text="Add Empty Event", command=self.add_empty_event)
        self.add_empty_event_button.grid(row=0, column=1)

        # 添加删除选中条目的按钮
        self.delete_event_button = tk.Button(self.event_frame, text="Delete Selected Event", command=self.delete_selected_event)
        self.delete_event_button.grid(row=0, column=2)


        # 创建表格控件
        self.event_tree = ttk.Treeview(root, columns=("Event ID", "Date", "Name", "Type", "Description", "Location", "Organizer", "Notes"), show='headings')
        self.event_tree.heading("Event ID", text="Event ID")
        self.event_tree.heading("Date", text="Date")
        self.event_tree.heading("Name", text="Name")
        self.event_tree.heading("Type", text="Type")
        self.event_tree.heading("Description", text="Description")
        self.event_tree.heading("Location", text="Location")
        self.event_tree.heading("Organizer", text="Organizer")
        self.event_tree.heading("Notes", text="Notes")
        self.event_tree.pack()  # 可能需要调整 columnspan 的值
        #self.show_all_events()

        # 为事件表格添加可编辑的功能
        self.event_tree.bind("<Double-1>", self.on_event_click)  # 双击进行编辑
        self.event_entry_edit = tk.Entry(root, bd=0)
        self.event_entry_edit.place(x=-100, y=-100)
        self.event_entry_edit.bind("<Return>", self.save_event_edit)

        # 创建一个容器来放置天体对象的按钮和表格
        self.object_frame = tk.Frame(root)
        self.object_frame.pack()

        # 添加显示所有天体对象的按钮
        self.show_all_objects_button = tk.Button(self.object_frame, text="Show All Objects", command=self.show_all_objects)
        self.show_all_objects_button.grid(row=0, column=0)

        # 添加添加空条目的按钮
        self.add_empty_object_button = tk.Button(self.object_frame, text="Add Empty Object", command=self.add_empty_object)
        self.add_empty_object_button.grid(row=0, column=1)

        # 添加删除选中条目的按钮
        self.delete_object_button = tk.Button(self.object_frame, text="Delete Selected Object", command=self.delete_selected_object)
        self.delete_object_button.grid(row=0, column=2)

        # 创建表格控件
        self.object_tree = ttk.Treeview(root, columns=("Object ID", "Name", "Type", "Mass", "Radius", "Distance", "Description", "Notes"), show='headings')
        self.object_tree.heading("Object ID", text="Object ID")
        self.object_tree.heading("Name", text="Name")
        self.object_tree.heading("Type", text="Type")
        self.object_tree.heading("Mass", text="Mass")
        self.object_tree.heading("Radius", text="Radius")
        self.object_tree.heading("Distance", text="Distance")
        self.object_tree.heading("Description", text="Description")
        self.object_tree.heading("Notes", text="Notes")
        self.object_tree.pack()

        # 为天体对象表格添加可编辑的功能
        self.object_tree.bind("<Double-1>", self.on_object_click)  # 双击进行编辑
        self.object_entry_edit = tk.Entry(root, bd=0)
        self.object_entry_edit.place(x=-100, y=-100)
        self.object_entry_edit.bind("<Return>", self.save_object_edit)

        # 添加计算按钮
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()


    def add_empty_observation(self):
        # 在表格中添加一条空记录
        self.observation_tree.insert("", "end", values=("", "", "", "", "", "", "", ""))

        # 调用后端类的添加方法，创建新的空记录
        self.observation_form.add_observation()
        self.show_all_observations()
        
    def delete_selected_observation(self):
        selected_items = self.observation_tree.selection()  # 获取选中的条目
        for item in selected_items:
            # 获取选中条目的ID
            id = self.observation_tree.item(item, 'values')[0]

            # 删除表格中的条目
            self.observation_tree.delete(item)

            # 调用后端方法删除数据库中的条目
            self.observation_form.remove_observation_by_id(id)

    # 观测记录部分的方法
    def show_all_observations(self):
        # 清空表格中现有的行
        for i in self.observation_tree.get_children():
            self.observation_tree.delete(i)

        # 获取所有观测记录
        observations = self.observation_form.get_all_observations()

        # 将观测记录添加到表格中
        for observation in observations:
            self.observation_tree.insert("", "end", values=(
                observation.get("ID"), 
                observation.get("Observation Date"), 
                observation.get("Location"), 
                observation.get("Celestial Body Name"), 
                observation.get("Celestial Body Type"), 
                observation.get("Observation Conditions"), 
                observation.get("Observer Name"), 
                observation.get("Notes")
            ))


    def on_observation_click(self, event):
        # 获取被点击的单元格的行列信息
        row_id = self.observation_tree.identify_row(event.y)
        column_id = self.observation_tree.identify_column(event.x)

        # 获取 Treeview 控件的绝对坐标
        tree_x = self.observation_tree.winfo_x()
        tree_y = self.observation_tree.winfo_y()

        # 显示输入框于相应位置
        x, y, width, height = self.observation_tree.bbox(row_id, column_id)
        self.entry_observation_edit.place(x=x + tree_x, y=y + tree_y, width=width, height=height)


        # 设置输入框的当前值
        self.entry_observation_edit.delete(0, tk.END)
        self.entry_observation_edit.insert(0, self.observation_tree.item(row_id, 'values')[int(column_id[1:]) - 1])
        self.entry_observation_edit.focus()

        # 保存当前编辑的行和列信息
        self.current_item = row_id
        self.current_column = int(column_id[1:]) - 1


    def save_observation_edit(self, event):
        # 获取输入框的值并更新到表格中
        new_value = self.entry_observation_edit.get()
        current_values = list(self.observation_tree.item(self.current_item, 'values'))
        current_values[self.current_column] = new_value
        self.observation_tree.item(self.current_item, values=current_values)

        # 隐藏输入框
        self.entry_observation_edit.place(x=-100, y=-100)

        # 更新后端数据
        self.update_backend_data(self.current_item, self.current_column, new_value)

    def update_backend_data(self, row_id, column_index, new_value):
        # 获取当前行的所有值
        values = self.observation_tree.item(row_id, 'values')

        # 从当前行获取ID
        id = values[0]  # 假设ID是在第一列

        # 根据列索引更新相应的参数
        observation_date = values[1] if column_index != 1 else new_value
        location = values[2] if column_index != 2 else new_value
        celestial_body_name = values[3] if column_index != 3 else new_value
        celestial_body_type = values[4] if column_index != 4 else new_value
        observation_conditions = values[5] if column_index != 5 else new_value
        observer_name = values[6] if column_index != 6 else new_value
        notes = values[7] if column_index != 7 else new_value

        # 重复此逻辑以处理其他列...

        # 调用 update_database_record 方法更新后端数据
        self.observation_form.update_database_record(
            id=id, 
            observation_date=observation_date, 
            location=location, 
            celestial_body_name=celestial_body_name, 
            celestial_body_type=celestial_body_type, 
            observation_conditions=observation_conditions, 
            observer_name=observer_name, 
            notes=notes
        )

    def add_empty_event(self):
        # 在表格中添加一条空记录
        self.event_tree.insert("", "end", values=("", "", "", "", "", "", "", ""))

        # 调用后端方法添加空记录
        self.event_form.add_event(
            event_id=None, 
            event_date=None, 
            event_name=None, 
            event_type=None, 
            event_description=None, 
            location=None, 
            organizer=None, 
            notes=None
        )
        self.show_all_events();
        
    def delete_selected_event(self):
        selected_items = self.event_tree.selection()  # 获取选中的条目
        for item in selected_items:
            # 获取选中条目的 Event ID
            event_id = self.event_tree.item(item, 'values')[0]

            # 删除表格中的条目
            self.event_tree.delete(item)

            # 调用后端方法删除数据库中的条目
            self.event_form.remove_event_by_id(event_id)

    def show_all_events(self):
        # 清空表格中现有的行
        for i in self.event_tree.get_children():
            self.event_tree.delete(i)

        # 获取所有天文事件
        events = self.event_form.get_all_events()  # 使用提供的方法

        # 将天文事件添加到表格中
        for event in events:
            self.event_tree.insert("", "end", values=(
                event.get("Event ID"), 
                event.get("Event Date"), 
                event.get("Event Name"),
                event.get("Event Type"),
                event.get("Event Description"),
                event.get("Location"),
                event.get("Organizer"),
                event.get("Notes")
            ))

    # 双击事件表格的处理方法
    def on_event_click(self, event):
        # 获取被点击的单元格的行列信息
        row_id = self.event_tree.identify_row(event.y)
        column_id = self.event_tree.identify_column(event.x)

        # 获取 Treeview 控件的绝对坐标
        tree_x = self.event_tree.winfo_x()
        tree_y = self.event_tree.winfo_y()

        # 显示输入框于相应位置
        x, y, width, height = self.event_tree.bbox(row_id, column_id)
        self.event_entry_edit.place(x=x+tree_x, y=y+tree_y, width=width, height=height)

        # 设置输入框的当前值
        self.event_entry_edit.delete(0, tk.END)
        self.event_entry_edit.insert(0, self.event_tree.item(row_id, 'values')[int(column_id[1:]) - 1])
        self.event_entry_edit.focus()

        # 保存当前编辑的行和列信息
        self.current_event_item = row_id
        self.current_event_column = int(column_id[1:]) - 1

    # 保存事件编辑的处理方法
    def save_event_edit(self, event):
        # 获取输入框的值并更新到表格中
        new_value = self.event_entry_edit.get()
        current_values = list(self.event_tree.item(self.current_event_item, 'values'))
        current_values[self.current_event_column] = new_value
        self.event_tree.item(self.current_event_item, values=current_values)

        # 隐藏输入框
        self.event_entry_edit.place(x=-100, y=-100)

        # 更新后端数据
        self.update_event_backend_data(self.current_event_item, self.current_event_column, new_value)
    
    def update_event_backend_data(self, row_id, column_index, new_value):
        # 获取当前行的所有值
        values = self.event_tree.item(row_id, 'values')

        # 从当前行获取 Event ID
        event_id = values[0]  # 假设 Event ID 在第一列

        # 根据列索引更新相应的参数
        event_date = values[1] if column_index != 1 else new_value
        event_name = values[2] if column_index != 2 else new_value
        event_type = values[3] if column_index != 3 else new_value
        event_description = values[4] if column_index != 4 else new_value
        location = values[5] if column_index != 5 else new_value
        organizer = values[6] if column_index != 6 else new_value
        notes = values[7] if column_index != 7 else new_value

        # 调用 update_database_record 方法更新后端数据
        self.event_form.update_database_record(
            event_id=event_id, 
            event_date=event_date, 
            event_name=event_name,
            event_type=event_type,
            event_description=event_description,
            location=location,
            organizer=organizer,
            notes=notes
        )


    def add_empty_object(self):
        # 在表格中添加一条空记录
        self.object_tree.insert("", "end", values=("", "", "", "", "", "", "", ""))

        # 调用后端方法添加空记录
        self.object_form.add_object()
        self.show_all_objects()

    def delete_selected_object(self):
        selected_items = self.object_tree.selection()  # 获取选中的条目
        for item in selected_items:
            # 获取选中条目的 Object ID
            object_id = self.object_tree.item(item, 'values')[0]

            # 删除表格中的条目
            self.object_tree.delete(item)

            # 调用后端方法删除数据库中的条目
            self.object_form.remove_object_by_id(object_id)

    def show_all_objects(self):
        # 清空表格中现有的行
        for i in self.object_tree.get_children():
            self.object_tree.delete(i)

        # 获取所有天体对象
        objects = self.object_form.get_all_objects()  # 假设这个方法返回所有天体对象的列表

        # 将天体对象添加到表格中
        for obj in objects:
            self.object_tree.insert("", "end", values=(
                obj.object_id, 
                obj.object_name, 
                obj.object_type, 
                obj.object_mass, 
                obj.object_radius, 
                obj.object_distance, 
                obj.object_description, 
                obj.notes
            ))

    # 双击天体对象表格的处理方法
    def on_object_click(self, event):
        # 获取被点击的单元格的行列信息
        row_id = self.object_tree.identify_row(event.y)
        column_id = self.object_tree.identify_column(event.x)

        # 获取单元格的位置和大小
        x, y, width, height = self.object_tree.bbox(row_id, column_id)

        # 获取 Treeview 控件的绝对坐标
        tree_x = self.object_tree.winfo_x()
        tree_y = self.object_tree.winfo_y()

        # 显示输入框于相应位置
        self.object_entry_edit.place(x=x+tree_x, y=y+tree_y, width=width, height=height)

        # 设置输入框的当前值
        self.object_entry_edit.delete(0, tk.END)
        self.object_entry_edit.insert(0, self.object_tree.item(row_id, 'values')[int(column_id[1:]) - 1])
        self.object_entry_edit.focus()

        # 保存当前编辑的行和列信息
        self.current_object_item = row_id
        self.current_object_column = int(column_id[1:]) - 1

    # 保存天体对象编辑的处理方法
    def save_object_edit(self, event):
        # 获取输入框的值并更新到表格中
        new_value = self.object_entry_edit.get()
        current_values = list(self.object_tree.item(self.current_object_item, 'values'))
        current_values[self.current_object_column] = new_value
        self.object_tree.item(self.current_object_item, values=current_values)

        # 隐藏输入框
        self.object_entry_edit.place(x=-100, y=-100)

        # 更新后端数据
        self.update_object_backend_data(self.current_object_item, self.current_object_column, new_value)
    def update_object_backend_data(self, row_id, column_index, new_value):
        # 获取当前行的所有值
        values = self.object_tree.item(row_id, 'values')

        # 从当前行获取 Object ID
        object_id = values[0]  # 假设 Object ID 在第一列

        # 根据列索引更新相应的参数
        object_name = values[1] if column_index != 1 else new_value
        object_type = values[2] if column_index != 2 else new_value
        object_mass = values[3] if column_index != 3 else new_value
        object_radius = values[4] if column_index != 4 else new_value
        object_distance = values[5] if column_index != 5 else new_value
        object_description = values[6] if column_index != 6 else new_value
        notes = values[7] if column_index != 7 else new_value

        # 调用 update_database_record 方法更新后端数据
        self.object_form.update_database_record(
            object_id=object_id, 
            object_name=object_name, 
            object_type=object_type,
            object_mass=object_mass,
            object_radius=object_radius,
            object_distance=object_distance,
            object_description=object_description,
            notes=notes
        )
        
    def calculate(self):
        self.object_form.calculate()
        # 显示尚未实现功能的提示消息
        messagebox.showinfo("Info", "This feature has not yet been implemented")

# 创建 Tkinter 窗口并运行
root = tk.Tk()
app = AstronomyManager(root)
root.mainloop()
