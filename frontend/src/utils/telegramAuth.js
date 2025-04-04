export function initTelegramLogin(callback) {
    window.TelegramLoginWidget = {
        dataOnauth: callback,
    };
    
    const script = document.createElement("script");
    script.src = "https://telegram.org/js/telegram-widget.js?7";
    script.setAttribute("data-telegram-login", "YOUR_BOT_USERNAME");
    script.setAttribute("data-size", "large");
    script.setAttribute("data-userpic", "true");
    script.setAttribute("data-request-access", "write");
    script.async = true;
    document.getElementById("telegram-login-container").appendChild(script);
}
