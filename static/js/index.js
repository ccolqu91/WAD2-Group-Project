
function register(){
        window.location.href="{% url 'survey_server:register' %}";

    }
function select(){
        window.location.href="{% url 'survey_server:select' %}";
}
function survey(){
 window.location.href="{% url 'survey_server:survey' %}";
}