<template>
  <div class="village-info">
    <!-- Navigation Tabs -->
    <div class="section-nav mb-4">
      <div class="nav-pills">
        <button
          v-for="(section, key) in sections"
          :key="key"
          class="nav-link"
          :class="{ active: activeSection === key }"
          @click="activeSection = key"
        >
          <i :class="section.icon" class="me-2"></i>
          {{ section.title }}
        </button>
      </div>
    </div>

    <!-- Content -->
    <div class="content-card">
      <component :is="sections[activeSection].component" />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import OverviewSection from './village-sections/OverviewSection.vue'
import TemplesSection from './village-sections/TemplesSection.vue'
import AgricultureSection from './village-sections/AgricultureSection.vue'
import FacilitiesSection from './village-sections/FacilitiesSection.vue'
import VoterInfoSection from './village-sections/VoterInfoSection.vue'

export default {
  name: 'VillageInfo',
  components: {
    OverviewSection,
    TemplesSection,
    AgricultureSection,
    FacilitiesSection,
    VoterInfoSection
  },
  setup() {
    const activeSection = ref('overview')

    const sections = {
      overview: {
        title: 'Overview',
        icon: 'fas fa-map-marker-alt',
        component: OverviewSection
      },
      temples: {
        title: 'Temples',
        icon: 'fas fa-place-of-worship',
        component: TemplesSection
      },
      agriculture: {
        title: 'Agriculture',
        icon: 'fas fa-seedling',
        component: AgricultureSection
      },
      facilities: {
        title: 'Facilities',
        icon: 'fas fa-building',
        component: FacilitiesSection
      },
      voters: {
        title: 'Voter Info',
        icon: 'fas fa-vote-yea',
        component: VoterInfoSection
      }
    }

    return {
      activeSection,
      sections
    }
  }
}
</script>

<style scoped>
.village-info {
  padding: 1rem 0;
}

.section-nav {
  overflow-x: auto;
}

.content-card {
  background: white;
  border-radius: var(--radius-md);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
}

@media (max-width: 768px) {
  .content-card {
    padding: 1.5rem;
  }
}
</style>

