<template>
    <div>
      <div>
        <h2 class="text-3xl my-8 font-extrabold text-center">{{title}}</h2>
        <h3 class="m-5 text-secondary text-center">{{ subTitle }}</h3>
        <h3 v-if="timestamp" class="m-5 text-secondary text-center">Dernière modification : {{ timestamp }} </h3>
      </div>
      <div class="flex justify-center">
          <Card class="h-[70vh] w-[95vw] md:w-[670px] max-w-[670px] overflow-y-scroll" no-fit>
              <Steps :nb-steps="nbSteps" :nb-steps-active="nbStepsActive" :nb-steps-lock="nbStepsLock" class="w-full"></Steps>
              <div class="divider"></div> 
              <slot></slot>
          </Card>
      </div>
      <div class="flex justify-center">
        <div class="flex justify-center md:justify-end md:w-[580px] mt-5">
          <ButtonPrimary v-if="buttonDisabled" @click="$emit('handleButtonClick')" disabled>{{buttonTitle}}</ButtonPrimary>
          <ButtonPrimary v-else @click="$emit('handleButtonClick')">{{buttonTitle}}</ButtonPrimary>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
defineProps({
  title: String,
  subTitle: String,
  nbSteps: Number,
  nbStepsActive: Number,
  nbStepsLock: Number,
  stepLock: Number,
  buttonTitle: String,
  buttonDisabled: Boolean,
  timestamp: String,
});

defineEmits(['handleButtonClick'])
</script>
  