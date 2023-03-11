import os
import csv
from .models import MenuItem, Restaurant


def populate_menu_items(restaurant_slug):
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_slug)
    except Restaurant.DoesNotExist:
        return
    
    directory_path = f'media/menus/{restaurant_slug}'
    csv_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            name_col_indices = {h: headers.index(h) for h in headers}
            
            for row in reader:
                if not row:
                    continue
                
                # Create a new menu item for the current row
                for item_type, name_col_index in name_col_indices.items():
                    item_name = row[name_col_index]
                    if item_name:
                        if item_type == 'ï»¿starters' or item_type not in ['mains', 'desserts','drinks']: #starter name not rendering correctly - so all other items are starters
                            item_type = 'starters'
                        MenuItem.objects.create(restaurant=restaurant, type=item_type, name=item_name)
