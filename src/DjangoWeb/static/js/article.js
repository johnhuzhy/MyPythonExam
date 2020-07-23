function addAction() {
  $("form").submit();
}

function upddelAction(id) {
  $("input[name='column_id']").val(id);
  $("form").submit();
}
