<template>
<div>
	<a href="https://www.target.com/p/playstation-5-console/-/A-81114595?clkid=f0187338N5ccc11ebb10e42010a246d22&lnm=81938&afid=Future%20PLC.&ref=tgt_adv_xasd0002">
		<li class="list-group-item" :class="{ 
			'bg-success': inStock, 
			'bg-warning': checkBack,
			'bg-danger': !(inStock || checkBack)
			}">
			<div class="row">
				<div id="name" class="d-flex justify-content-between">
					<p :class="{ active : inStock }"><strong>Target</strong></p>
					<i v-show="checkBack" class="fas fa-flushed fa-3x"></i>
					<i v-show="inStock" class="fas fa-grin-stars fa-3x"></i>
					<i v-show="!(inStock || checkBack)" class="fas fa-skull-crossbones fa-3x"></i>
				</div>
				<span v-if="inStock || checkBack" id="restock-date-true">
					<p>CHECK ATHENS LOCATION!</p>
					<p>Aisle 47 Block F OR Aisle 50 Block F</p>
				</span>
				<span v-else id="restock-date-false">Out of stock</span>
			</div>
		</li>
	</a>
</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Walmart',
	data: function() {
		return {
			inStock: false,
			checkBack: false,
		}
	},

	created() {
		axios.get('http://127.0.0.1:8000/target')
			.then(response => {
				// Base stock information needs to be reversed, since its asking if it is out of stock
				// which obviously means it is out of stock
				this.inStock = !response['data']['product']['fulfillment']['is_out_of_stock_in_all_store_locations'];

				// Athens specific information
				let local_status = response['data']['product']['fulfillment']['store_options']["0"];
				let local_pickup = local_status['order_pickup']['availability_status'];
				let local_in_store_only = local_status['in_store_only']['availability_status'];
				let local_ship_to_store = local_status['ship_to_store']['availability_status'];

				let shipping_status = 
					response['data']['product']['fulfillment']['shipping_options']['availability_status'];

				const OOS = "OUT_OF_STOCK";
				if (local_pickup !== OOS || local_in_store_only !== OOS || shipping_status !== OOS)
					this.checkBack = true;
				
				if (local_ship_to_store !== "UNAVAILABLE")
					this.checkBack = true;

			})
			.catch(err => console.log(err));
	},

	methods: {
		fetchData: function() {

		}
	}


}
</script>

<style>

</style>