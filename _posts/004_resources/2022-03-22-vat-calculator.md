---
layout: post
title: "VAT Calculator"
author: "adakar"
categories: resources
tags: [moms, toll, fortolling, vat, value added tax, tax]
image: assets/images/004_resources/mva.png
---

In Norway, everything you buy is taxed by a 25% value added tax (VAT). This is usually baked into the price in Norway, making it functionally invisible. 
For products being imported from other countries, the VAT is added as it goes through customs. There is also a handling fee, usually in the range of 100-250 NOK, depending on the carrier used.
The cost of shipping must also be included when calculating how much your imported purchase will cost after VAT is added.

Some items can be affected by tarifs, mostly textiles and food. For a comprehensive list of what is covered by duties, see [the Norwegian Customs agency's website](https://www.toll.no/no/bedrift/import/importguide/#varer_som_er_tollbelagt). 
In practice, this is rarely relevant for airsoft.

You will often find that the total will end up being lower than the calcluator predicts, this is usually due to customs being lazy and not the calculator being wrong. 



<script type="text/javascript">
function calc() {
    var price = document.getElementById("price");
    var priceValue = parseFloat(price.value);
  
    var total = (priceValue * 1.25) +150;
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
