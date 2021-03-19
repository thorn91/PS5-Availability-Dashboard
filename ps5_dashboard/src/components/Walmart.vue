<template>
<div>
	<a href="https://www.walmart.com/ip/PlayStation-5-Console/363472942">
		<li class="list-group-item" :class="{ 
			'bg-success': inStock, 
			'bg-warning': checkBack,
			'bg-danger': !(inStock || checkBack)
			}">
			<div class="row">
				<div v-if="!error">
					<div id="name" class="d-flex justify-content-between">
						<p :class="{ active : inStock }"><strong>{{ store }}</strong></p>
						<i v-show="checkBack" class="fas fa-flushed fa-3x"></i>
						<i v-show="inStock" class="fas fa-grin-stars fa-3x"></i>
						<i v-show="!(inStock || checkBack)" class="fas fa-frown fa-3x"></i>
					</div>
					<span v-if="inStock" id="restock-date-true">{{ stockDate }}</span>
					<span v-else id="restock-date-false">Out of stock</span>
				</div>
				<div v-else>
					<div id="name" class="d-flex justify-content-between">
						<p><strong>{{ store }}</strong></p>
						<i class="fas fa-dizzy fa-3x"></i>
					</div>
						<p><strong>Error fetching results!</strong></p>
				</div>

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
			store: 'Walmart',
			stockDate: '',
			inStock: false,
			checkBack: false,
			error: false,
		}
	},

	created() {
		axios.get('http://127.0.0.1:8000/walmart')
			.then(response => {
				this.stockDate = response['data']['stock_date'];
				this.inStock = response['data']['stock'];
				this.checkBack = response['data']['check_back'];
			})
			.catch(err => {
				console.log(err)
				this.error = true;
			});
	},

	methods: {
		fetchData: function() {

		}
	}


}
</script>

<style>

</style>