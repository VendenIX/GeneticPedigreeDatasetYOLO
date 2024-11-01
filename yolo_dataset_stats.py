import os

import cv2
import pandas as pd
import yaml


class DatasetAnalyzer:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_yaml(config_path)
        self.stats = {}

    def load_yaml(self, file_path):
        """Charge un fichier YAML et retourne le contenu."""
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def get_image_sizes_and_stats(self, images_dir):
        """Retourne les tailles moyennes des images dans un dossier et le nombre total d'images."""
        widths, heights = [], []
        for img_name in os.listdir(images_dir):
            img_path = os.path.join(images_dir, img_name)
            img = cv2.imread(img_path)
            if img is not None:
                heights.append(img.shape[0])
                widths.append(img.shape[1])
        return widths, heights, len(widths)

    def analyze_dataset(self):
        train_dir = self.config['train']
        val_dir = self.config['val']
        test_dir = self.config['test']
        classes = self.config['names']
        
        self.stats = {'train': {}, 'val': {}, 'test': {}, 'total': {}}
        total_counts = {class_id: 0 for class_id in classes}
        total_image_count = 0

        for split, img_dir in [('train', train_dir), ('val', val_dir), ('test', test_dir)]:
            widths, heights, image_count = self.get_image_sizes_and_stats(img_dir)
            mean_width = sum(widths) / len(widths) if widths else 0
            mean_height = sum(heights) / len(heights) if heights else 0
            total_image_count += image_count

            self.stats[split]['mean_width'] = mean_width
            self.stats[split]['mean_height'] = mean_height
            self.stats[split]['image_count'] = image_count

            label_dir = img_dir.replace('images', 'labels')
            class_counts = {class_id: 0 for class_id in classes}
            for label_file in os.listdir(label_dir):
                with open(os.path.join(label_dir, label_file), 'r') as f:
                    for line in f:
                        class_id = int(line.split()[0])
                        class_counts[class_id] += 1
                        total_counts[class_id] += 1

            self.stats[split]['class_counts'] = class_counts
            self.stats[split]['total_individuals'] = sum(class_counts.values())

        # calcul des moyennes et sommes pour le dataset complet
        all_widths, all_heights = [], []
        for img_dir in [train_dir, val_dir, test_dir]:
            widths, heights, _ = self.get_image_sizes_and_stats(img_dir)
            all_widths.extend(widths)
            all_heights.extend(heights)

        self.stats['total']['mean_width'] = sum(all_widths) / len(all_widths) if all_widths else 0
        self.stats['total']['mean_height'] = sum(all_heights) / len(all_heights) if all_heights else 0
        self.stats['total']['class_counts'] = total_counts
        self.stats['total']['image_count'] = total_image_count
        self.stats['total']['total_individuals'] = sum(total_counts.values())

    def display_stats(self):
        """Affiche les statistiques du dataset."""
        classes = self.config['names']
        print("Statistiques du dataset :")
        for split in self.stats:
            print(f"\n{split.capitalize()} set:")
            print(f"  Taille moyenne des images : {self.stats[split]['mean_width']} x {self.stats[split]['mean_height']}")
            print(f"  Nombre total d'images : {self.stats[split].get('image_count', 0)}")
            print(f"  Nombre total d'individus dans toutes les classes : {self.stats[split].get('total_individuals', 0)}")
            print(f"  Nombre d'individus par classe :")
            for class_id, count in self.stats[split]['class_counts'].items():
                print(f"    Classe {classes[class_id]} : {count}")

                
"""
# Utilisation dans un notebook

# charger et analyser le dataset
config_path = 'config.yaml'  # path vers le fichier de configuration YAML
analyzer = DatasetAnalyzer(config_path)
analyzer.analyze_dataset()
analyzer.display_stats()
"""