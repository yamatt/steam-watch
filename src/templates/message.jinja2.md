{% macro real_time_trains_link(service) -%}
[👀 Real Time Trains](https://www.realtimetrains.co.uk/service/gb-nr:{{ service.train_uid }}/{{ service.pass | rtt_url_dt }}/detailed)
{%- endmacro -%}

{%- macro add_to_google_calendar_link(tiploc, service) -%}
[🗓️ Add to Google Calendar](https://calendar.google.com/calendar/u/0/r/eventedit?text=Steam+train+at+{{ tiploc[service.tiploc] | capitalise | urlquote }}&dates={{ service.pass | google_calendar_url_dt }}/{{ service.pass | google_calendar_url_dt }}&details={{ service.train_uid }}+–+{{ tiploc[service.first_stop.atoc] | capitalise | urlquote }}+→+{{ tiploc[service.end_stop.atoc] | capitalise | urlquote }}&location={{ tiploc[service.tiploc] | capitalise | urlquote }}+platform+{{ service.platform }})
{%- endmacro -%}

{%- for service in data -%}
🚂 {{ service.train_uid }} – {{ tiploc[service.first_stop.atoc] | capitalise }} → {{ tiploc[service.end_stop.atoc] | capitalise }} 📍 {{ tiploc[service.tiploc] | capitalise }} platform {{ service.platform }} 🕗 {{ service.pass }} {{ real_time_trains_link(service) }} {{ add_to_google_calendar_link(tiploc, service) }}

{% endfor -%}
