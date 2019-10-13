//script que permite generar una tabla de datos con la información traducida
$.fn.dataTableExt.ofnSearch['string'] = function (data) {
    return !data ?
        '' :
        typeof data === 'string' ?
            data
                .replace(/\n/g, ' ')
                .replace(/á/g, 'a')
                .replace(/é/g, 'e')
                .replace(/í/g, 'i')
                .replace(/ó/g, 'o')
                .replace(/ú/g, 'u')
                .replace(/ê/g, 'e')
                .replace(/î/g, 'i')
                .replace(/ô/g, 'o')
                .replace(/è/g, 'e')
                .replace(/ï/g, 'i')
                .replace(/ü/g, 'u')
                .replace(/ç/g, 'c')
                .replace(/Á/g, 'A')
                .replace(/É/g, 'E')
                .replace(/Í/g, 'I')
                .replace(/Ó/g, 'O')
                .replace(/Ú/g, 'U')
            :
            data;
};

if ($('.responsive-table').length !== 0) {
    var thArray = [];

    $('.table thead > tr > th').each(function () {
        thArray.push($(this).text())
    });
    var opciones = false;
    if ('Opciones' == thArray[thArray.length - 1]) {
        opciones = true;
    }

    function excluir_columna(elemento) {
        if (elemento) {
            return ':not(:last-child)'

        } else {
            return ':visible'
        }

    }

    $('.responsive-table').dataTable({
        dom: 'lBfrtip',
        buttons: [
            {
                extend: 'copy',
                className: 'btn-sm',
                text: 'Copiar',
                exportOptions: {
                    columns: excluir_columna(opciones)
                }
            },
            {
                extend: 'csv',
                className: 'btn-sm',
                exportOptions: {
                    columns: excluir_columna(opciones)
                }
            },
            {
                extend: 'excel',
                className: 'btn-sm',
                exportOptions: {
                    columns: excluir_columna(opciones)
                }
            },
            /*{
                extend: 'pdf',
                className: 'btn-sm',
                exportOptions: {
                    columns: excluir_columna(opciones)
                }
            },*/
            {
                extend: 'print',
                className: 'btn-sm',
                text: 'Imprimir',
                exportOptions: {
                    columns: excluir_columna(opciones)
                }
            }
        ],
        "language": {
            "decimal": "",
            "emptyTable": "No hay registros en el sistema",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 a 0 de 0 registros",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ registros",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Registro no encontrado",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": activate to sort column ascending",
                "sortDescending": ": activate to sort column descending"
            },
            buttons: {
                copyTitle: 'Copiado a portapapeles',
                copySuccess: {
                    _: '%d lineas copiadas',
                    1: '1 linea copiada'
                }
            }
        },
        colReorder: true,
        keys: true,
        rowReorder: false,
        select: true
    });
}