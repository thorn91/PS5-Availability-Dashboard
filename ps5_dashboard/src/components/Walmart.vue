<template>
<div>
	<a href="https://www.walmart.com/ip/PlayStation-5-Console/363472942">
		<li class="list-group-item" :class="{ 
			'bg-success': inStock, 
			'bg-warning': checkBack,
			'bg-danger': !(inStock || checkBack)
			}">
			<div class="row">
				<div id="name" class="d-flex justify-content-between">
					<p :class="{ active : inStock }"><strong>Walmart</strong></p>
					<i v-show="checkBack" class="fas fa-flushed fa-3x"></i>
					<i v-show="inStock" class="fas fa-grin-stars fa-3x"></i>
					<i v-show="!(inStock || checkBack)" class="fas fa-skull-crossbones fa-3x"></i>
				</div>
				<span v-if="inStock" id="restock-date-true">{{ stockDate }}</span>
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
			stockDate: '',
			inStock: false,
			checkBack: false,
		}
	},

	created() {
		axios.get('http://127.0.0.1:8000/walmart')
			.then(response => {
				console.log(response['data'])
				this.stockDate = response['data']['stock_date'];
				this.inStock = response['data']['stock'];
				this.checkBack = response['data']['check_back'];
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