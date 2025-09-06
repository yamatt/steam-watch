{% macro real_time_trains_url(service) -%}
https://www.realtimetrains.co.uk/service/gb-nr:{{ service.train_uid }}/{{ service.pass | rtt_url_dt }}/detailed
{%- endmacro -%}

{%- macro add_to_google_calendar_url(tiploc, service) -%}
https://calendar.google.com/calendar/u/0/r/eventedit?text=Steam+train+at+{{ tiploc[service.tiploc] | capitalise | urlquote }}&dates={{ service.pass | google_calendar_url_dt }}/{{ service.pass | google_calendar_url_dt }}&details={{ service.train_uid }}+–+{{ tiploc[service.first_stop.atoc] | capitalise | urlquote }}+→+{{ tiploc[service.end_stop.atoc] | capitalise | urlquote }}&location={{ tiploc[service.tiploc] | capitalise | urlquote }}+platform+{{ service.platform }}
{%- endmacro -%}

{%- for service in services -%}
🚂 {{ service.train_uid }} – {{ tiploc[service.first_stop.atoc] | capitalise }} → {{ tiploc[service.end_stop.atoc] | capitalise }} 📍 {{ tiploc[service.tiploc] | capitalise }} platform {{ service.platform }} 🕗 {{ service.pass | friendly_dt }} [👀 Real Time Trains]({{ real_time_trains_url(service) }}) [🗓️ Add to Google Calendar]({{ add_to_google_calendar_url(tiploc, service) }})

{% endfor -%}
