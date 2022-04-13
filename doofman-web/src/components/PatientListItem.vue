<script lang="ts">
    import { defineComponent } from 'vue'

    export default defineComponent({

        props: {
            patient: {
              type: Object
            }
        },
        data() {
          return {
            id: this.patient?._id.$oid
          }
        },
        methods: {

        },
        mounted() {

        },
        created() {

        },
        computed: {
          getPatientStatus(): string {
            return this.patient?.status == 1 ? "Active": "Inactive"
          },
          setStatusStyles(): string {
            return this.patient?.status == 2 ? 'bg-warning': 'bg-primary'
          }
        }
    })
</script>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="card w-50 mx-auto my-2">
    <h5 class="card-header">{{ patient.name }}</h5>
    <div class="card-body">
      <p class="my-0"><span class="fw-bold pe-1">E-mail:</span>{{ patient.email }}</p>
      <p class="my-0"><span class="fw-bold pe-1">Telephone number:</span>{{ patient.telephone_number }}</p>
      <RouterLink v-bind:to="'/appointment/' + id" class="card-link text-decoration-none">Appointments</RouterLink>
      <RouterLink :to="'/consult/' + id" class="card-link text-decoration-none">Consults</RouterLink>
      <RouterLink :to="'/payment/' + id" class="card-link text-decoration-none">Payments</RouterLink>
    </div>
    <div class="card-footer">
      <span class="badge" :class="setStatusStyles">{{ getPatientStatus }}</span>
    </div>
  </div>
</template>

<style>

</style>
