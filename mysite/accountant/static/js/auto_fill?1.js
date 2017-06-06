if (!$) {
    $ = django.jQuery;
}

function get_value(target_id) {
	var val = $('#' + target_id).val();
	var rst = parseFloat(val)
	if (rst ) {
		return rst;
	}
	return 0;
}


function updateAccountPayable(e) {
	var target_id = e.currentTarget.id;
	var price_id = null;
	var amount_id = null;
	var account_payable_id = null;

	if (target_id.endsWith('price')) {
		price_id = target_id;
		amount_id = target_id.replace('price', 'amount');
		account_payable_id = target_id.replace('price', 'account_payable');
	} else if (target_id.endsWith('amount')) {
		amount_id = target_id;
		price_id = target_id.replace('amount', 'price');
		account_payable_id = target_id.replace('amount', 'account_payable');
	}

	var price = get_value(price_id);
	var amount = get_value(amount_id);
	$('#' + account_payable_id).val(price * amount).change();
}


function updateTotalPayable() {
	var total = 0;
	var num_product_orders = $('#id_productorder_set-TOTAL_FORMS').val();
	for (var i = 0; i < num_product_orders; i++) {
		var account_payable_id = "id_productorder_set-" + i.toString() + "-account_payable";
		total += get_value(account_payable_id);
	}

	var num_processing_fees = $('#id_processingfee_set-TOTAL_FORMS').val();
	for (var i = 0; i < num_processing_fees; i++) {
		var account_payable_id = "id_processingfee_set-" + i.toString() + "-account_payable";
		total += get_value(account_payable_id);
	}
	$('#id_total_payable').val(total);
}

function updateTotalAmount() {
	var num_product_orders = $('#id_productorder_set-TOTAL_FORMS').val();
	var total = 0;
	for (var i = 0; i < num_product_orders; i++) {
		var amount_id = "id_productorder_set-" + i.toString() + "-amount";
		total += get_value(amount_id);
	}
	var num_customer_product = $('#id_customerproduct_set-TOTAL_FORMS').val();
	for (var i = 0; i < num_customer_product; i++) {
		var amount_id = "id_customerproduct_set-" + i.toString() + "-amount";
		total += get_value(amount_id);
	}
	$('#id_total_amount').val(total);
}

$(document).ready(function() {
	console.log("ready!");
	var num_product_orders = $('#id_productorder_set-TOTAL_FORMS').val();
	for (var i = 0; i < num_product_orders; i++) {
		var price_id = "id_productorder_set-" + i.toString() + "-price";
		var amount_id = "id_productorder_set-" + i.toString() + "-amount";
		var account_payable_id = "id_productorder_set-" + i.toString() + "-account_payable";
		$('#' + price_id).on('input', updateAccountPayable);
		$('#' + amount_id).on('input', updateAccountPayable);
		$('#' + amount_id).on('input', updateTotalAmount);
		$('#' + account_payable_id).on('change', updateTotalPayable);
	}

	var num_processing_fees = $('#id_processingfee_set-TOTAL_FORMS').val();
	for (var i = 0; i < num_processing_fees; i++) {
		var price_id = "id_processingfee_set-" + i.toString() + "-price";
		var amount_id = "id_processingfee_set-" + i.toString() + "-amount";
		var account_payable_id = "id_processingfee_set-" + i.toString() + "-account_payable";
		$('#' + price_id).on('input', updateAccountPayable);
		$('#' + amount_id).on('input', updateAccountPayable);
		$('#' + account_payable_id).on('change', updateTotalPayable);
	}

	var num_customer_product = $('#id_customerproduct_set-TOTAL_FORMS').val();
	for (var i = 0; i < num_customer_product; i++) {
		var amount_id = "id_customerproduct_set-" + i.toString() + "-amount";
		$('#' + amount_id).on('input', updateTotalAmount);
	}
	
});

(function($) {
    $(document).on('formset:added', function(event, $row, formsetName) {
        
    	var row_id = $row[0].id;
    	var price_id = "id_" + row_id + "-price";
		var amount_id = "id_" + row_id + "-amount";
		var account_payable_id = "id_" + row_id + "-account_payable";
		$('#' + price_id).on('input', updateAccountPayable);
		$('#' + amount_id).on('input', updateAccountPayable);
		$('#' + amount_id).on('input', updateTotalAmount);
		$('#' + account_payable_id).on('change', updateTotalPayable);
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        // Row removed
        updateTotalPayable();
        updateTotalAmount();
    });
})(django.jQuery);
console.log("lalalalalala");
