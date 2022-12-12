django.jQuery().ready(function(){
    loadCidade(django.jQuery("#id_estado").val());

    django.jQuery("#id_estado").on('change', function(e) {
        loadCidade(e.target.value);
    });

    function loadCidade(estado) {
        django.jQuery("#id_cidade option").remove();

        if (estado != "" && estado != undefined) {
            django.jQuery.ajax({
                method: 'get',
                url: '/api/cidades/'+estado,
                success: (res) => {
                    data = JSON.parse(res);
                    data.forEach(cidade => {
                        django.jQuery("#id_cidade").append(`
                            <option ${cidade.fields.capital ? 'selected' : ''} 
                                value=${cidade.pk}>${cidade.fields.nome}
                            </option>
                        `);
                    });
                    
                    if (data.length == 0){
                        django.jQuery("#id_cidade").append("<option value>---------</option>");
                    }
                }
            });
        } else {
            django.jQuery("#id_cidade").append("<option value>---------</option>");
        }
    }
});
