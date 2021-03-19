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
				<span v-if="inStock" id="restock-date-true">
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
				this.inStock = response['data']['product']['fufillment']['is_out_of_stock_in_all_store_locations']

				// Athens specific information
				let local_status = response['data']['product']['fufillment']
				let local_avb_status = local_status['store_options']['0']
				let shipping_status = response['data']['product']['fufillment']['shipping_options']
				
				// I apologize to myself
				if ((local_avb_status['order_pickup']['availability_status'] 
					|| local_avb_status['in_store_only']['availability_status']) !== "OUT_OF_STOCK" 
					|| local_avb_status['ship_to_store']['availability_status']  !== "UNAVAILABLE"
					|| shipping_status['availability_status'] !== "OUT_OF_STOCK"
					|| shipping_status['reason_code'] !== "OUT_OF_STOCK") {
						this.checkBack = true;
				}

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