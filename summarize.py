from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


def summarize(text):
    
    model_id = "aiautomationlab/german-news-title-gen-mt5"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    headline_generator = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
        num_beams=5
    )

    input_text = "summarize: " + text
    generated_headline = headline_generator(input_text)[0]["summary_text"]

    return(generated_headline)




text = "Der Rüssel gehört zu den auffälligsten anatomischen Merkmalen der Elefanten. Er stellt eine Verwachsung der Nase mit der Oberlippe dar, welche bereits im Fötalalter miteinander verschmelzen.[40][41] Äußerlich bildet er einen muskulären Schlauch ohne knöchernen Unterbau, der von den Nasengängen durchzogen wird. Am unteren Ende des „Schlauches“ treten diese durch die Nasenlöcher heraus. Das Füllvolumen beträgt bei einem Asiatischen Elefanten mit rund 1,8 m langem Rüssel etwa 2,2 bis 3,1 l. Umgeben werden die Nasenlöcher von einer breiten, ebenen Fläche, an deren Rändern „fingerförmige“ Ausstülpungen aufragen. Beim Afrikanischen Elefanten sind dies zwei gegenständige „Finger“ am oberen und unteren Rand, beim Asiatischen nur ein einzelner am oberen. Das Wollhaarmammut besaß ebenfalls nur einen „Finger“ an der oberen Kante, wies aber gegenüberstehend einen breiten, schaufelförmigen Zipfel auf. Die Ausstülpungen dienen primär als Greiforgan. Prinzipiell besteht der Rüssel aus Haut, Haaren und Muskeln sowie Blut- und Lymphgefäßen beziehungsweise Nerven und einem geringen Anteil an Fett. Knorpelgewebe ist nur am Nasenansatz ausgebildet. Als hochsensitives Organ wird der Rüssel von zwei Nerven durchzogen, dem Nervus facialis und dem Nervus trigeminus. Die Muskeln wirken unterstützend. Es sind zwei Muskeltypen ausgebildet, die einerseits längs, andererseits quer beziehungsweise diagonal verlaufen. Teils wurde angenommen, dass 40.000 bis 60.000 zu Bündeln verflochtene Muskeln den Rüssel bewegen, Extrapolationen an einem sezierten Tier ergaben dagegen bis zu 150.000 Muskelbündel. Zu den Hauptmuskelgruppen gehören die vorderen levators proboscidis, die am Stirnbein ansetzen, durch den gesamten Rüssel verlaufen und diesen zum Heben bringen. Weiterhin bedeutend sind die depressores proboscidis. Diese nehmen den unteren Bereich des Rüssels ein und sind stark mit den Quermuskeln und der Haut verbunden. Dabei scheinen beim Rüssel des Afrikanischen Elefanten mehr ringartige Quermuskeln aufzutreten, so dass dieser beweglicher und „lappiger“ wirkt als beim Asiatischen Elefanten. Evolutiv entstand der Rüssel schon sehr früh in der Stammesgeschichte der Rüsseltiere. Die Herausbildung des Rüssels führte zu einigen anatomischen Änderungen im Schädelbereich, die vor allem der Ausbildung der massiven Muskulatur geschuldet sind. Die markanteste findet sich in einer außerordentlichen Reduktion des Nasenbeins und einer stark vergrößerten Nasenöffnung. Sekundär kam es auch zur Rückbildung des vorderen Gebisses. Da der Rüssel die Distanz vom Kopf zum Erdboden überbrückt, die der kurze Hals nicht bewerkstelligen kann, ist ersterer unabdingbar bei der Nahrungsaufnahme. Die Schneidezähne, die bei zahlreichen Säugetieren hauptsächlich in schneidender Weise bei der Nahrungsaufnahme Einsatz finden, hatten bei den Rüsseltieren dadurch keine vordergründige Funktion mehr. Mit Ausnahme der Stoßzähne entwickelten sie sich deshalb zurück. Darüber hinaus ist der Rüssel ein Multifunktionsorgan, welches als Tast- und Greiforgan, zur Atmung beziehungsweise Geruchswahrnehmung sowie als Waffe und Drohmittel, zusätzlich auch als Saug- und Druckpumpe beim Trinken dient. Durch die an seinem unteren Ende befindlichen Tasthaare eignet er sich auch als Tastorgan, mit dem die Tiere kleinste Unebenheiten wahrnehmen können. Er findet zudem Einsatz bei der Kontaktaufnahme zu Artgenossen in der Herde, etwa bei den komplexen Begrüßungsritualen und beim Spiel. Mit dem Rüssel werden Staub und Schmutz auf der Haut verteilt, was zum Schutz vor der starken Sonneneinstrahlung und vor Insekten geschieht. Des Weiteren wird der Rüssel zum Greifen von Gegenständen benutzt, beispielsweise, um sie zum Mund zu führen. Mit seiner Hilfe kann ein Tier Äste und Pflanzen aus bis zu sieben Meter Höhe erreichen. Ähnlich einem Giraffenhals verdoppelt er damit seine Streckhöhe. Gelegentlich dient der Rüssel beim Baden oder Schwimmen als eine Art Schnorchel, zum Riechen wird er hoch in die Luft gehalten. Ausgebildete Arbeitselefanten können mit Hilfe des Rüssels und mit Unterstützung der Stoßzähne sowie in Zusammenarbeit mit dem Elefantenführer Gegenstände von erheblichem Gewicht manipulieren, heben und bewegen."
s = summarize(text)
print(s)

