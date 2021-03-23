<template>
<div>
	<a href="https://www.samsclub.com/s/playstation%205?altQuery=7330129&clubId=8194&offset=0&rootDimension=pcs_availability%253AOnlinepipsymbcategory%253A7330129pipsymbProduct%2520Type%253AVideo%2520Game%2520Consoles&searchCategoryId=all&searchTerm=playstation+5&selectedFilter=all&sortKey=relevance&sortOrder=1">
		<li class="list-group-item m-1 rounded-3 shadow-lg" :class="{ 
			'bg-success': inStock, 
			'bg-warning': checkBack,
			'bg-danger': !(inStock || checkBack)
			}">
			<div class="row">
				<div v-if="!error">
					<div id="name" class="d-flex justify-content-between">
						<p :class="{ active : inStock }"><strong>{{ store }}</strong></p>
						<i v-show="inStock" class="fas fa-grin-stars fa-3x"></i>
						<i v-show="!(inStock || checkBack)" class="fas fa-frown fa-3x"></i>
					</div>
					<span v-if='!inStock' id="restock-date-false"><p>Out of stock</p></span>
					<span v-else id="in-stock-true"><p>In Stock!  Note: sizeable handlers fee for non members.</p></span>
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
	name: 'SamsClub',
	data: function() {
		return {
			store: 'Sam\'s Club',
			inStock: false,
			error: false,
		}
	},

	created() {
		axios.get('http://127.0.0.1:8000/walmart')
			.then(response => {
				this.inStock = response['data']['stock'];
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