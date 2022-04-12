<script lang="ts">
    import { defineComponent } from 'vue'

    export default defineComponent({

        props: {
            patient: {
              type: Object,
              default: () => {return {}}
            }
        },
        data() {
            
        },
        methods: {

        },
        mounted() {

        },
        created() {

        }
    })
</script>

<template>
  <div class="card w-75 mx-auto my-2" :class="patient.status == 2 ? 'border-warning': ''">
    <h5 class="card-header">{{ patient.name }}</h5>
    <div class="card-body">
      <p class="my-0"><span class="fw-bold pe-1">E-mail:</span>{{ patient.email }}</p>
      <p class="my-0"><span class="fw-bold pe-1">Telephone number:</span>{{ patient.telephone_number }}</p>
      <a href="#" class="card-link">Appointments</a>
      <a href="#" class="card-link">Consults</a>
      <a href="#" class="card-link">Payments</a>
    </div>
    <div class="card-footer">
      {{ patient.status == 1 ? "Active": "Inactive"}}
    </div>
  </div>
</template>

<style>

</style>
