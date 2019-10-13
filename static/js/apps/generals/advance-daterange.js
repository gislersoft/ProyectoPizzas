/* Uso de advance-daterange
    <div class="advance-daterange btn btn-white btn-block">
        <span></span>
        <i class="fa fa-angle-down fa-fw"></i>
    </div>
*
*
* */

//Traducir fechas manejadas con moment a español
moment.locale('es');

//fecha inicial
$('.advance-daterange span').html(moment().subtract(29, 'days').format('MMMM D, YYYY') + ' - ' + moment().format('MMMM D, YYYY'));

//configuración
$('.advance-daterange').daterangepicker({
    format: 'MM/DD/YYYY',
    startDate: moment().subtract(29, 'days'),
    endDate: moment(),
    //minDate: '01/01/2012',
    //maxDate: '12/31/2015',
    //dateLimit: { years: 1000 },
    showDropdowns: true,
    showWeekNumbers: true,
    timePicker: false,
    timePickerIncrement: 1,
    timePicker12Hour: true,
    ranges: {
        'Hoy': [moment(), moment()],
        'Ayer': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
        'Últimos 7 días': [moment().subtract(6, 'days'), moment()],
        'Últimos 30 días': [moment().subtract(29, 'days'), moment()],
        'Este mes': [moment().startOf('month'), moment().endOf('month')],
        'Último mes': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
    },
    opens: 'right',
    drops: 'down',
    buttonClasses: ['btn', 'btn-md'],
    applyClass: 'btn-primary',
    cancelClass: 'btn-default',
    separator: ' a ',
    linkedCalendars: false,
    autoApply: true,
    locale: {
        applyLabel: 'Seleccionar',
        cancelLabel: 'Cancelar',
        fromLabel: 'Desde',
        toLabel: 'Hasta',
        customRangeLabel: 'Personalizada',
        daysOfWeek: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        firstDay: 1
    }
}, function (start, end, label) {
    $('.advance-daterange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
});