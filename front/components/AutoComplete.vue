<template>
    <div>
      <Combobox :value="selected" :default-value="people[0]" @update:model-value="updateSelected">
        <div class="relative mt-1">
          <div
            class="relative w-full cursor-default rounded-full bg-base-100 text-left sm:text-sm"
          >
            <ComboboxInput
              class="w-[250px] rounded-full border-[1px] shadow-md py-2 pl-3 pr-10 text-sm leading-5"
              :displayValue="(person) => `${person.firstname} ${person.name}`"
              @change="state.query = $event.target.value"
            />
            <ComboboxButton
              class="absolute inset-y-0 right-0 flex items-center pr-2"
            >
              <img src="../public/people.svg" alt="people" class="h-5 w-5"/>
            </ComboboxButton>
          </div>
          <TransitionRoot
            leave="transition ease-in duration-100"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
            @after-leave="state.query = ''"
          >
            <ComboboxOptions
              class="absolute mt-1 max-h-60 w-full z-10 overflow-auto rounded-lg bg-base-100 py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm"
            >
              <div
                v-if="filteredPeople.length === 0 && state.query !== ''"
                class="relative cursor-default select-none px-4 py-2 text-secondary"
              >
                Nothing found.
              </div>
  
              <ComboboxOption
                v-for="person in filteredPeople"
                as="template"
                :key="person.id"
                :value="person"
                v-slot="{ selected, active }"
              >
                <li
                  class="relative cursor-default select-none py-2 pl-3 pr-4"
                  :class="{
                    'bg-primary text-base-100': active,
                    'text-secondary': !active,
                  }"
                >
                  <span
                    class="block truncate"
                    :class="{ 'font-medium': selected, 'font-normal': !selected }"
                  >
                    {{ person.firstname }} {{  person.name }}
                  </span>
                </li>
              </ComboboxOption>
            </ComboboxOptions>
          </TransitionRoot>
        </div>
      </Combobox>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import {
    Combobox,
    ComboboxInput,
    ComboboxButton,
    ComboboxOptions,
    ComboboxOption,
    TransitionRoot,
  } from '@headlessui/vue'
  

  const people = [
    { id: 1, firstname:'Wade', name:"Cooper", email: "wade.cooper@example.com" },
    { id: 2, firstname: 'Arlene', name:"Mccoy", email: "arlene.mccoy@example.com" },
    { id: 3, firstname: 'Devon', name: 'Webb', email: "devon.webb@example.com" },
    { id: 4, firstname:'Tom', name: 'Cook', email: "tom.cook@example.com" },
    { id: 5, firstname: 'Tanya', name: 'Fox', email: "tanya.fox@example.com" },
    { id: 6, firstname:'Hellen', name: 'Schmidt', email: "hellen.schmidt@example.com" },
];

  const props = defineProps({
      selected: Object
  })

  const emit = defineEmits(['update:selected'])

  const state = reactive({
      query: '',
  })


  onMounted(() => {
     emit('update:selected', people[0])
  })

  const updateSelected = (person) => {
    emit('update:selected', person)
  }

  let filteredPeople = computed(() =>
    state.query === ''
      ? people
      : people.filter((person) =>
      (person.firstname +
          person.name)
            .toLowerCase()
            .replace(/\s+/g, '')
            .includes(state.query.toLowerCase().replace(/\s+/g, ''))
        )
  )
  </script>
  