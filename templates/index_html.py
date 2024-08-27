# Autogenerated file
def render(work, cool):
    yield """

<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>ESPlorer</title>
    <link rel=\"stylesheet\" href=\"static/css/index.css\" />
</head>
<body>
    <div class=\"wrapper\">
        <div class=\"container\">
            <div class=\"device\">
                <div class=\"device__header\">
                    Управление электрокамином
                </div>
                <label>Volume:</label>
                <p id=\"volume\">0</p><br>
                <label>Brightness:</label>
                <p id=\"brightness\">0</p></br>
                <label>Cooler:</label>
                <p id=\"cLabel\">0</p><br>
                <div class=\"device__body\">
                    <div class=\"left-buttons\">
                        <div class=\"left-slider\"><br>
                            <label>Вкл/выкл</label><br>
                            <label class=\"switch\">
                                <input type=\"checkbox\" id=\"power\" onclick=\"workSwitch()\" """
    if work == 1:
        yield """ checked """
    yield """>
                                <span class=\"slider round\"></span>
                            </label><br>
                            <label></label>
                        </div>
                        <button class=\"btns\" id=\"soundp\" onclick=\"soundInc()\">
                            Звук+
                        </button>
                        <button class=\"btns\" id=\"brightp\" onclick=\"brightInc()\">
                            Яркость+
                        </button>
                    </div>
                    <div class=\"right-buttons\">
                        <button class=\"btns\" id=\"cooler\" onclick=\"coolerInc()\">
                            Кулер
                        </button>
                        <button class=\"btns\" id=\"soundm\" onclick=\"soundDecr()\">
                            Звук-
                        </button>
                        <button class=\"btns\" id=\"brightn\" onclick=\"brightDecr()\">
                            Яркость-
                        </button>
                    </div>
                </div>
                
                <div class=\"device__circles\">
                    <button class=\"device__circles-1\" onclick=\"yellow()\">
                    </button>
                    <button class=\"device__circles-2\" onclick=\"blue()\">
                    </button>
                    <button class=\"device__circles-3\" onclick=\"red()\">
                    </button>
                    <button class=\"device__circles-4\" onclick=\"orange()\">
                    </button>
                    <button class=\"device__circles-5\" onclick=\"green()\">
                    </button>
                </div>
                <div class=\"device__footer\">
                    LLC \"ELECTRONIC DEVICES\", UZBEKISTAN
                </div>
            </div>
        </div>
    </div>
    
    <script src=\"static/js/index.js\"></script>
</body>
</html>
"""
