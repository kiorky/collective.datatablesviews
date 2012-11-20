if(typeof(datatablesviewsmapdt_tables) == "undefined") {
  var datatablesviewsmapdt_asInitVals = new Array();
  var datatablesviewsmapdt_tables = new Array();
}
jq(document).ready(function(){
  var datatablesviewsmapdt_elems = jq(".datatable-wrapper table");
  datatablesviewsmapdt_elems.each(function(i, elem){
    var jelem = jq(elem);
    var id = jelem.attr("id");
    var searchcontrols = $("tr.search-controls", jelem);
    datatablesviewsmapdt_asInitVals[id] = new Array();
    nbcolumns = $('td', $("tbody tr", jelem)[0]).length;
    ratio = Math.floor(100/nbcolumns);
    cdefs = new Array();
    for (i=0;i<nbcolumns;i++) {
      cdefs[cdefs.length] = {
        aTargets: [i],
        bSearchable: true,
        sWidth: "1%"
      };
    }
    datatablesviewsmapdt_tables[id] = jelem.dataTable(
    {bJQueryUI: true,
     aaSorting: [],
     bAutoWidth: false,
     sDom: 'lpfrti<"clear">T',
     oLanguage: {"sUrl": "@@collective.js.datatables.translation"},
     oTableTools: {"sSwfPath": "++resource++jquery.datatables/extras/TableTools/media/swf/copy_csv_xls_pdf.swf"},
     bSort: true,
     bPaginate: true,
     bSortCellsTop: true,
     sPaginationType: "full_numbers",
     aoColumnDefs: cdefs
    });
  });
}); 
