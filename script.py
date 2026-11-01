import argparse
import os
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def export_isolated_clusters(image_path, output_dir="output", prefix="layer"):
    print(f"Processando a imagem: {image_path}...")
    
    # Cria o diretório de saída se ele não existir
    os.makedirs(output_dir, exist_ok=True)
    
    img = Image.open(image_path).convert("RGBA")
    arr = np.array(img)
    
    h, w, _ = arr.shape
    rgb = arr[:, :, :3]
    pixels = rgb.reshape(-1, 3)
    
    print("Executando clusterização K-Means...")
    kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
    labels = kmeans.fit_predict(pixels).reshape(h, w)
    
    # Foca nos clusters de interesse continental (0 e 4)
    target_clusters = [0, 4]
    
    for cluster_id in target_clusters:
        mask = (labels == cluster_id)
        
        # Cria um buffer transparente
        layer_arr = np.zeros((h, w, 4), dtype=np.uint8)
        layer_arr[mask] = arr[mask]
        
        # Salva cada imagem dentro da pasta de output
        output_filename = os.path.join(output_dir, f"{prefix}_cluster_{cluster_id}.png")
        layer_img = Image.fromarray(layer_arr, 'RGBA')
        layer_img.save(output_filename)
        print(f"-> Gerado com sucesso: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gera imagens PNG isoladas por cluster de cor em uma pasta de output.")
    parser.add_argument("input_image", type=str, help="Caminho para a imagem de entrada")
    parser.add_argument("-d", "--dir", type=str, default="output", help="Diretório de saída (padrão: output)")
    parser.add_argument("-p", "--prefix", type=str, default="continente", help="Prefixo para os arquivos de saída")
    
    args = parser.parse_args()
    export_isolated_clusters(args.input_image, args.dir, args.prefix)
    