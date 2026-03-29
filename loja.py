from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Hospital dos Óculos</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <!-- Ícones -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

   <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #000; /* fundo preto */
        text-align: center;
        margin: 0;
        color: white;
    }

    .container {
        padding: 20px;
    }

    .logo {
        width: 230px;
        border-radius: 50%;
        margin-top: 20px;
        border: 3px solid #ff6600;
    }

    h1 {
        margin: 25px 0 5px;
        color: #ff6600; /* laranja */
    }

    p {
        color: #ccc;
        margin-bottom: 20px;
    }

    .btn {
        display: block;
        width: 90%;
        max-width: 400px;
        margin: 12px auto;
        padding: 15px;
        border-radius: 12px;
        background-color: #ff6600; /* laranja */
        color: black; /* texto preto */
        text-decoration: none;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        transition: 0.2s;
    }

    .btn:hover {
        background-color: #ff8533; /* laranja mais claro */
        transform: scale(1.03);
    }

    .btn i {
        margin-right: 10px;
    }

    /* Botões específicos */
    .maps {
        background-color: #111; /* preto mais claro */
        color: #ff6600;
        border: 2px solid #ff6600;
    }

    .insta {
        background-color: #222;
        color: #ff6600;
        border: 2px solid #ff6600;
    }

    .phone {
        background-color: #111;
        color: #ff6600;
        border: 2px solid #ff6600;
    }
</style>
    </head>

    <body>
        <div class="container">

            <!-- LOGO -->
            <img src="https://github.com/pardinho04/hospital-dos-oculos/blob/main/Captura%20de%20tela%202026-03-28%20234922.png?raw=true" class="logo">

            <h1>Hospital Dos Óculos</h1>
            <p>Especialistas em consertos há mais de 30 anos!</p>

            <!-- BOTÕES -->
            <a class="btn" href="https://wa.me/5544999026468" target="_blank">
                <i class="fab fa-whatsapp"></i> Nosso WhatsApp
            </a>

            <a class="btn maps" href="https://www.google.com/maps/place/Hospital+dos+%C3%93culos+Maring%C3%A1/@-23.3915037,-51.9589998,17z/data=!3m1!4b1!4m6!3m5!1s0x94ecd7c3d18061e1:0xed2dcf3d7e932dd!8m2!3d-23.3915086!4d-51.9564249!16s%2Fg%2F11tjqn43q8?entry=ttu&g_ep=EgoyMDI2MDMyNC4wIKXMDSoASAFQAw%3D%3D" target="_blank">
                <i class="fas fa-map-marker-alt"></i> Ver Localização
            </a>

            <a class="btn insta" href="https://www.instagram.com/hospitaldosoculosmaringa?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank">
                <i class="fab fa-instagram"></i> Instagram
            </a>

            <a class="btn phone" href="tel:+5544999026468">
                <i class="fas fa-phone"></i> Ligar Agora
            </a>

        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    import os
    # O Render define a porta automaticamente, por isso usamos os.environ
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
