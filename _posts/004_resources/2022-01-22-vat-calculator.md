---
layout: post
title: "VAT Calculator"
author: "adakar"
categories: resources
tags: [moms, toll, airsoft, fortolling, fortollning, vat, value added tax, tax]
image: assets/images/toll.png
---

For everything you buy you will need to pay a 25% value added tax (VAT), this is usually baked into the price in Norway, making it invisible. For products outside the border the VAT is added as it goes through customs. There is also a handling fee, usually 130nok. 
You must also include shipping in your VAT calculations.

Some items can be affected by tarifs, mostly textiles and food. A comprehensive list of what is covered by duty click [here](https://www.toll.no/no/bedrift/import/importguide/#varer_som_er_tollbelagt). This is rarely relevant for airsoft.

You will often find that the total will end up being lower than the calcluator predicts, this is usually due to customs being lazy and not the calculator being wrong. 



<script type="text/javascript">
function calc() {
    var price = document.getElementById("price");
    var priceValue = parseFloat(price.value);
  
    var total = (priceValue * 1.25) +130;
    document.getElementById("total").value = total.toString();
    
}
</script>

<div>
	<b>Purchase sum:</b>
	<br>
		<input type="text" placeholder="Price + shipping in NOK" id="price"> <button type="button" onclick="javascript:calc();">Calculate</button>
	<br>
	<b>Total including VAT and handling:</b>
	<br>
		<input type="text" placeholder="Total cost in NOK" id="total" disabled/> 
	<br>
</div>
