<template>
  <div class="app">
    <AppHeader />

    <main class="main-content">
      <div class="container-fluid">
        <!-- Navigation Tabs -->
        <ul v-if="!selectedWard" class="nav nav-pills mb-4" role="tablist">
          <li class="nav-item" role="presentation">
            <button 
              class="nav-link" 
              :class="{ active: activeTab === 'search' }"
              @click="handleTabChange('search')"
              type="button"
            >
              <i class="fas fa-search me-2"></i>
              Search Voters
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button 
              class="nav-link" 
              :class="{ active: activeTab === 'dashboard' }"
              @click="handleTabChange('dashboard')"
              type="button"
            >
              <i class="fas fa-chart-bar me-2"></i>
              Dashboard
            </button>
          </li>
        </ul>

        <!-- Search Voters Tab -->
        <SearchVoters 
          v-if="activeTab === 'search' && votersData && !selectedWard"
          :voters-data="votersData"
        />
        
        <!-- Dashboard Tab -->
        <Dashboard 
          v-if="activeTab === 'dashboard' && votersData && !selectedWard"
          :voters-data="votersData"
          @view-ward="handleViewWard"
        />
        
        <!-- Ward Voters View -->
        <WardVoters
          v-if="selectedWard && votersData"
          :ward-data="selectedWard"
          @back="handleBack"
          @navigate="handleNavigate"
        />
        
        <!-- Loading State -->
        <div v-if="!votersData && !loadingError" class="text-center py-5">
          <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
          <p class="mt-3 text-muted">
            <i class="fas fa-spinner fa-spin me-2"></i>
            Loading voter data...
          </p>
        </div>
        
        <!-- Error State -->
        <div v-if="loadingError" class="alert alert-danger text-center">
          <i class="fas fa-exclamation-triangle me-2"></i>
          <strong>Error loading data:</strong> {{ loadingError }}
          <br>
          <small>Please check the browser console for more details.</small>
        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<script>
import { ref, onMounted, watch, nextTick } from 'vue'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import SearchVoters from './components/SearchVoters.vue'
import Dashboard from './components/Dashboard.vue'
import WardVoters from './components/WardVoters.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter,
    SearchVoters,
    Dashboard,
    WardVoters
  },
  setup() {
    const activeTab = ref('search')
    const votersData = ref(null)
    const selectedWard = ref(null)
    const loadingError = ref(null)

    onMounted(async () => {
      try {
        const response = await fetch('/wards_data.json')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        votersData.value = data
        console.log('Voter data loaded:', Object.keys(data).length, 'wards')
      } catch (error) {
        console.error('Error loading voter data:', error)
        loadingError.value = error.message
      }
    })

    const scrollToTop = () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }

    const handleTabChange = (tab) => {
      activeTab.value = tab
      selectedWard.value = null
      nextTick(() => {
        scrollToTop()
      })
    }

    const handleViewWard = (wardKey) => {
      if (votersData.value && votersData.value[wardKey]) {
        selectedWard.value = votersData.value[wardKey]
        activeTab.value = 'dashboard'
        nextTick(() => {
          scrollToTop()
        })
      }
    }

    const handleBack = () => {
      selectedWard.value = null
      nextTick(() => {
        scrollToTop()
      })
    }

    const handleNavigate = (tab) => {
      activeTab.value = tab
      selectedWard.value = null
      nextTick(() => {
        scrollToTop()
      })
    }

    // Watch for tab changes and scroll to top
    watch(activeTab, () => {
      nextTick(() => {
        scrollToTop()
      })
    })

    // Watch for selectedWard changes and scroll to top
    watch(selectedWard, () => {
      nextTick(() => {
        scrollToTop()
      })
    })

    return {
      activeTab,
      votersData,
      selectedWard,
      loadingError,
      handleTabChange,
      handleViewWard,
      handleBack,
      handleNavigate
    }
  }
}
</script>
