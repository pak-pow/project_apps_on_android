import csv
import os
import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

FILENAME = "bale.csv"
HEADERS = ["Name", "Item", "Price", "How Many?", "Total", "Time"]

def create_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(HEADERS)

class MainScreen(Screen):
    def read_records(self):
        create_file()
        try:
            with open(FILENAME, "r", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                records = list(reader)

            if not records:
                self.show_popup("No Records", "There are no records to show.")
                return

            msg = ""
            for row in records:
                msg += f"{row['Name']} | {row['Item']} = {row['Price']} x {row['How Many?']} = {row['Total']} | {row['Time']}\n"

            self.show_popup("All Records", msg)

        except Exception as e:
            self.show_popup("Error", str(e))

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message),
                      size_hint=(0.9, 0.9), auto_dismiss=True)
        popup.open()

class AddRecordScreen(Screen):
    def add_record(self):
        name = self.ids.name_input.text.title().strip()
        item = self.ids.item_input.text.title().strip()
        price = self.ids.price_input.text.strip()
        quantity = self.ids.quantity_input.text.strip()

        if not all([name, item, price, quantity]):
            self.show_popup("Error", "All fields are required.")
            return

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            self.show_popup("Error", "Invalid number in price or quantity.")
            return

        total = price * quantity
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [name, item, price, quantity, total, now_str]

        create_file()
        with open(FILENAME, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)

        self.show_popup("Success", "Record added successfully.")

        # Clear fields
        self.ids.name_input.text = ""
        self.ids.item_input.text = ""
        self.ids.price_input.text = ""
        self.ids.quantity_input.text = ""

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message),
                      size_hint=(0.7, 0.5), auto_dismiss=True)
        popup.open()

class SearchScreen(Screen):
    def search_record(self):
        name = self.ids.search_input.text.title().strip()
        create_file()

        with open(FILENAME, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            matches = [row for row in reader if row["Name"] == name]

        if matches:
            result = ""
            for row in matches:
                result += f"{row['Name']} | {row['Item']} = {row['Price']} x {row['How Many?']} = {row['Total']}\n"
            self.ids.search_results.text = result
        else:
            self.ids.search_results.text = f"No record found for '{name}'."

class DeleteScreen(Screen):
    def delete_record(self):
        name = self.ids.delete_input.text.title().strip()
        create_file()

        with open(FILENAME, "r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            records = [row for row in reader if row and row[0] != name]

        with open(FILENAME, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(records)

        self.ids.delete_status.text = f"{name} has been deleted (if existed)."
        self.ids.delete_input.text = ""

class UtangApp(App):
    def build(self):
        create_file()
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(AddRecordScreen(name="add"))
        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(DeleteScreen(name="delete"))
        return sm

if __name__ == "__main__":
    UtangApp().run()
