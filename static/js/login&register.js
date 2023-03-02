 function manager(){
        document.user.action="{% url 'survey_server:manager' %}";
        document.user.submit();
    }
     function customer(){
        document.user.action="{% url 'survey_server:customer' %}";
        document.user.submit();
    }

    function login(){
          window.location.href="{% url 'survey_server:login' %}";
    }
     function register(){
        window.location.href="survey_server/register.html";

    }