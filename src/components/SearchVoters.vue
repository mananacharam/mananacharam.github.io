<template>
  <div class="search-voters">
    <div class="card">
      <div class="card-body">
        <div class="section-header mb-4">
          <h2 class="section-title">
            <i class="fas fa-search me-2 text-primary"></i>
            Search Voters
          </h2>
          <p class="section-subtitle text-muted">
            Find voters by name or EPIC number across all wards
          </p>
        </div>
        
        <div class="search-container">
          <div class="input-group input-group-lg search-input-group">
            <input
              type="text"
              class="form-control search-input"
              placeholder="Search by name or EPIC number..."
              v-model="searchQuery"
              @keyup.enter="performSearch"
              @input="performSearch"
            />
            <button class="btn btn-primary search-btn" type="button" @click="performSearch">
              <i class="fas fa-search me-2"></i>
              <span class="search-btn-text">Search</span>
            </button>
          </div>
        </div>

        <div v-if="searchResults.length > 0" class="alert alert-info d-flex align-items-center mb-4 border-0">
          <i class="fas fa-info-circle me-2 fs-5"></i>
          <span class="fw-semibold">Found <strong class="text-primary">{{ searchResults.length }}</strong> result(s)</span>
        </div>

        <div v-if="searchResults.length > 0" class="results">
          <div 
            v-for="(voter, index) in searchResults" 
            :key="index"
            class="card mb-3 border-0"
          >
            <div class="card-body p-3 p-md-4">
              <div class="d-flex flex-column flex-md-row justify-content-between align-items-start mb-3">
                <div class="mb-2 mb-md-0">
                  <h5 class="card-title mb-2 h6 h-md-5">
                    <i class="fas fa-user-circle text-primary me-2"></i>
                    <span class="d-block d-md-inline">{{ voter.name }}</span>
                  </h5>
                  <span class="badge bg-primary rounded-pill">
                    <i class="fas fa-map-marker-alt me-1"></i>
                    {{ voter.ward }}
                  </span>
                </div>
              </div>
              
              <div class="row g-2 g-md-3">
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-users me-1"></i>
                      Relationship
                    </small>
                    <strong class="small d-md-block">{{ voter.relationship_type }}: {{ voter.relationship_name }}</strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-birthday-cake me-1"></i>
                      Age & Gender
                    </small>
                    <strong class="small d-md-block">
                      {{ voter.age }} years, 
                      <i :class="voter.sex === 'M' ? 'fas fa-mars text-primary' : voter.sex === 'F' ? 'fas fa-venus text-danger' : 'fas fa-transgender text-success'"></i>
                      {{ voter.sex === 'M' ? 'Male' : voter.sex === 'F' ? 'Female' : 'Other' }}
                    </strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-home me-1"></i>
                      Door No.
                    </small>
                    <strong class="small d-md-block">{{ voter.door_no || 'N/A' }}</strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100 bg-light">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-id-card me-1"></i>
                      EPIC No.
                    </small>
                    <strong class="text-primary small d-md-block">{{ voter.epic_no }}</strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-hashtag me-1"></i>
                      A.C No.
                    </small>
                    <strong class="small d-md-block">{{ voter.ac_no }}</strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-hashtag me-1"></i>
                      PS No.
                    </small>
                    <strong class="small d-md-block">{{ voter.ps_no }}</strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-hashtag me-1"></i>
                      SL No.
                    </small>
                    <strong class="small d-md-block">{{ voter.sl_no }}</strong>
                  </div>
                </div>
                
                <div class="col-12 col-sm-6 col-md-6 col-lg-4">
                  <div class="border rounded p-2 p-md-3 h-100">
                    <small class="text-muted d-block mb-1 small">
                      <i class="fas fa-list-ol me-1"></i>
                      Serial No.
                    </small>
                    <strong class="small d-md-block">{{ voter.serial_no }}</strong>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-if="hasSearched && searchResults.length === 0" class="text-center py-5">
          <div class="mb-3">
            <i class="fas fa-search fa-4x text-muted opacity-50"></i>
          </div>
          <h5 class="text-muted">No voters found</h5>
          <p class="text-muted">Try adjusting your search query</p>
        </div>

        <div v-if="!hasSearched" class="text-center py-5">
          <div class="mb-3">
            <i class="fas fa-hand-point-up fa-4x text-primary opacity-50"></i>
          </div>
          <h5 class="text-muted">Enter a search query to find voters</h5>
          <p class="text-muted">
            Search by voter name or EPIC number
          </p>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'SearchVoters',
  props: {
    votersData: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const searchQuery = ref('')
    const hasSearched = ref(false)
    const searchResults = ref([])

    const allVoters = computed(() => {
      const voters = []
      for (const [wardKey, wardData] of Object.entries(props.votersData)) {
        const wardNumber = wardKey.replace('ward_', '')
        wardData.voters.forEach(voter => {
          voters.push({
            ...voter,
            ward: wardData.ward_no,
            wardKey: wardKey
          })
        })
      }
      return voters
    })

    const performSearch = () => {
      hasSearched.value = true
      const query = searchQuery.value.trim().toLowerCase()
      
      if (!query) {
        searchResults.value = []
        hasSearched.value = false
        return
      }

      // Search both name and EPIC number
      searchResults.value = allVoters.value.filter(voter => 
        voter.name.toLowerCase().includes(query) ||
        voter.epic_no.toLowerCase().includes(query)
      )
    }

    return {
      searchQuery,
      hasSearched,
      searchResults,
      performSearch
    }
  }
}
</script>

<style scoped>
.search-input-group {
  display: flex;
  flex-wrap: nowrap;
  width: 100%;
}

.search-input {
  flex: 1;
  min-width: 0;
  width: 100%;
  box-sizing: border-box;
}

.search-btn {
  white-space: nowrap;
  flex-shrink: 0;
}

.search-container {
  width: 100%;
  box-sizing: border-box;
  overflow: visible;
}

@media (max-width: 768px) {
  .search-container {
    padding: 1rem;
    margin: 0;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }

  .search-input-group {
    flex-direction: column;
    gap: 0.75rem;
    width: 100%;
    overflow: visible;
  }

  .search-input {
    width: 100% !important;
    max-width: 100%;
    border-radius: var(--radius) !important;
    padding: 0.875rem 1rem;
    font-size: 1rem;
    box-sizing: border-box;
    -webkit-appearance: none;
    appearance: none;
  }

  .search-btn {
    width: 100% !important;
    max-width: 100%;
    border-radius: var(--radius) !important;
    padding: 0.875rem 1rem;
    font-size: 1rem;
    box-sizing: border-box;
  }

  .search-btn-text {
    display: inline-block;
  }
}

@media (max-width: 480px) {
  .search-container {
    padding: 0.75rem;
    margin: 0 -0.5rem;
    width: calc(100% + 1rem);
    max-width: none;
  }

  .search-input {
    font-size: 16px; /* Prevents zoom on iOS */
    width: 100% !important;
    max-width: 100%;
  }

  .search-btn {
    width: 100% !important;
    max-width: 100%;
  }
}
</style>
