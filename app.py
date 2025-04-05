from flask import Flask, render_template, request, redirect
import json 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/cadastar", methods = ["GET", "POST"])
def cadastar():
    if request.method == "POST":
            titulo = request.form["titulo"]
            conteudo = request.form["conteudo"]

            with open("noticias.json", "r") as file:
                dados = json.load(file)
            noticias = dados.get("noticias", [])

            proximo_id = len(noticias) + 1

            nova_noticia = {
                "id": proximo_id, 
                "titulo": titulo, 
                "conteudo": conteudo
            }

            noticias.append(nova_noticia)

            dados["noticias"] = noticias
            with open("noticias.json", "u") as file:
                json.dump(dados, file, indent=4)

            return redirect("/cadastrar")

    return render_template("cadastrar.html")

@app.route("/noticias")
def noticia():
    with open('noticias.json', "p") as file:
        dados = json.load(file)
    noticias = dados.get("noticias", [])

    return render_template("noticias.html", noticias=noticias)

if __name__ == "__main__":
    app.run(debug=True)