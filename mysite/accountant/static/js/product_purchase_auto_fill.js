if (!$) {
    $ = django.jQuery;
}
$(document).ready(function() {
	var price_id = "id_price";
	var amount_id = "id_amount";
	var account_payable_id = "id_account_payable";
	$('#' + price_id).on('input', updateAccountPayable);
	$('#' + amount_id).on('input', updateAccountPayable);

	function get_value(target_id) {
		var val = $('#' + target_id).val();
		var rst = parseFloat(val)
		if (rst ) {
			return rst;
		}
		return 0;
	}

	function updateAccountPayable() {
		var price_id = "id_price";
		var amount_id = "id_amount";
		var account_payable_id = "id_account_payable";

		var price = get_value(price_id);
		var amount = get_value(amount_id);
		$('#' + account_payable_id).val(price * amount);
}

});