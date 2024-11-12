from itembox import ItemBox
from person import Person
from healthbar import HealthBar
class World:
    def __init__(self):
        self.obstacle_list = []
        
    def process_data(self, data, image_list, tile_size, item_box_group, item_box_images, enemy_group):
        
        for i, row in enumerate(data):
            for j, tile in enumerate(row):
                if tile >= 0:
                    
                    img = image_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = j * tile_size
                    img_rect.y = i * tile_size
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        pass
                        #TODO Add Water
                    elif tile >= 11 and tile <= 14:
                        pass
                        # TODO Add Decoration
                    elif tile == 15:
                        player = Person("player", j * tile_size, i * tile_size, 50, 10)
                        health_bar = HealthBar(10,10, player.health, player.health)
                    elif tile == 16:
                        enemy = Person("enemy", j * tile_size, i * tile_size, 20, 0)
                        enemy_group.add(enemy)
                    
                    elif tile == 17:
                        item_box = ItemBox('Ammo', j * tile_size, i * tile_size,item_box_images)
                        item_box_group.add(item_box)
                    elif tile == 18:
                        item_box = ItemBox('Grenade', j * tile_size, i * tile_size,item_box_images)
                        item_box_group.add(item_box)
                    elif tile == 19:
                        item_box = ItemBox('Health', j * tile_size, i * tile_size,item_box_images)
                        item_box_group.add(item_box)
                    elif tile == 20:
                        pass
                        #TODO Add Exit
                        
        return player, health_bar
    def draw(self, screen):
        for tile in self.obstacle_list:
            screen.blit(tile[0], tile[1])
            
                        
                    
            