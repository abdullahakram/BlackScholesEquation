# Black Scholes Equation

Die Black-Scholes-Gleichung ist eine mathematische Formel zur Berechnung des theoretischen Preises von europäischen Kauf- und Verkaufsoptionen. Sie wurde in den 1970er Jahren von Fischer Black und Myron Scholes entwickelt und später von Robert Merton erweitert. Die Gleichung basiert auf der Annahme, dass der Preis des Basiswerts einer geometrischen Brownschen Bewegung folgt.

Die Black-Scholes-Gleichung ist eine partielle Differentialgleichung, die die Entwicklung des Optionspreises im Laufe der Zeit beschreibt. Sie berücksichtigt den aktuellen Aktienkurs, den Ausübungspreis der Option, die Zeit bis zum Verfall, den risikofreien Zinssatz und die Volatilität des Aktienkurses. Die Gleichung ist gegeben durch:

$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$

wobei:

$V$ ist der Preis der Option in Abhängigkeit von der Zeit $t$ und dem Preis des Basiswerts $S$
$\sigma$ ist die Volatilität des Preises des Basiswerts
$r$ ist der risikofreie Zinssatz
Der erste Term der Gleichung stellt den zeitlichen Verfall des Optionswertes dar. Der zweite Term steht für die Diffusion des Aktienkurses, die proportional zur Volatilität im Quadrat ist. Der dritte Term stellt die Drift des Aktienkurses aufgrund des risikolosen Zinssatzes dar. Der letzte Term stellt den Gegenwartswert der erwarteten Auszahlung der Option bei Fälligkeit dar.

Mit der Black-Scholes-Gleichung lässt sich der beizulegende Zeitwert einer europäischen Kauf- oder Verkaufsoption berechnen, indem die partielle Differentialgleichung für einen bestimmten Satz von Eingangsparametern gelöst wird. Die Lösung ergibt den theoretischen Optionspreis, der mit dem Marktpreis verglichen werden kann, um festzustellen, ob die Option über- oder unterbewertet ist. Die Gleichung ist in der Finanzwelt weit verbreitet und hat die Entwicklung der Optionspreistheorie und das Verständnis der Finanzmärkte maßgeblich beeinflusst.
