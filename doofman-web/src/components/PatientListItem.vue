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
        id: this.patient?._id.$oid,
        showEditModal: false,
        mode: "add"
      }
    },
    methods: {
      toggleModal(show: boolean) {
        this.showEditModal = show;
      },
      setAddMode() {
        this.mode = "add";
      },
      setEditMode() {
        this.mode = "edit";
        this.toggleModal(true);
      }
    },
    mounted() {

    },
    created() {

    },
    computed: {
      getPatientStatus(): string {
        return this.patient?.status == 1 ? "Active": "Inactive";
      },
      setStatusStyles(): string {
        return this.patient?.status == 2 ? 'bg-warning': 'bg-primary';
      }
    }
})
</script>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import PatientModal from '@/components/PatientModal.vue'
</script>

<template>
  <div class="card w-50 mx-auto my-2">
    <h5 class="card-header">{{ patient.name }}</h5>
    <div class="card-body d-flex">
      <div class="flex-grow-1">
        <p class="my-0"><span class="fw-bold pe-1">E-mail:</span>{{ patient.email }}</p>
        <p class="my-0"><span class="fw-bold pe-1">Telephone number:</span>{{ patient.telephone_number }}</p>
        <RouterLink v-bind:to="'/appointments/' + id" class="card-link text-decoration-none">Appointments</RouterLink>
        <RouterLink :to="'/consult/' + id" class="card-link text-decoration-none">Consults</RouterLink>
        <RouterLink :to="'/payment/' + id" class="card-link text-decoration-none">Payments</RouterLink>
      </div>
      <div class="flex-shrink-0">
        <p class="text-end py-0 my-0"><a href="#" class="text-decoration-none" @click="setEditMode">Edit</a></p>
      </div>
    </div>
    <div class="card-footer">
      <span class="badge" :class="setStatusStyles">{{ getPatientStatus }}</span>
    </div>
    <PatientModal v-if="showEditModal" :patient="patient" :mode="mode"></PatientModal>
    <button v-if="showEditModal" @click="toggleModal(false)" class="btn btn-secondary m-1">Cancel</button>
  </div>
</template>

<style>

</style>
