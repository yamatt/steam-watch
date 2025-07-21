{% for service in data %}
🚂 {{ service.train_uid }} – {{ service.first_stop.atoc }} → {{ service.end_stop.atoc }} 📍 {{ service.tiploc }} platform {{ service.platform }} 🕗 {{ service.pass }} [Add to Google Calendar](https://calendar.google.com/calendar/u/0/r/eventedit?text=Steam+Train+at+{{ service.tiploc }}&dates={{ service.pass }}/{{ service.pass }}&details={{ service.train_uid }}+–+{{ service.first_stop.atoc }}+→+{{ service.end_stop.atoc }}&location={{ service.tiploc }}+platform+{{ service.platform }})
{% endfor -%}
