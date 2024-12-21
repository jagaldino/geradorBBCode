from flask import Flask, render_template, request

app = Flask(__name__)

def gerar_bbcode(equipe, artigo, motivo, tipo_carta):
    cores = {
        "Alerta": "#FF9900",
        "Notificação Interna": "#FF6600",
        "Advertência Escrita": "#FF3300",
        "Remoção": "#CC0000",
        "Exoneração": "#990000",
    }

    bbcode = (
        f"[center][b][color={cores[tipo_carta]}]{tipo_carta.upper()}[/color][/b][/center]\n"
        f"[b]Equipe:[/b] {equipe}\n"
        f"[b]Artigo:[/b] {artigo}\n"
        f"[b]Motivo:[/b] {motivo}\n"
    )

    return bbcode


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        equipe = request.form["equipe"]
        artigo = request.form["artigo"]
        motivo = request.form["motivo"]
        tipo_carta = request.form["tipo_carta"]

        bbcode = gerar_bbcode(equipe, artigo, motivo, tipo_carta)
        return render_template("index.html", bbcode=bbcode)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
