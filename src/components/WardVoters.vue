<template>
  <div class="ward-voters">
    <div class="card mb-3">
      <div class="card-body">
        <div class="d-flex align-items-center justify-content-between flex-wrap gap-3">
          <div class="d-flex align-items-center flex-wrap gap-2">
            <button class="btn btn-sm btn-outline-secondary" @click="$emit('back')">
              <i class="fas fa-arrow-left me-2"></i>
              Back
            </button>
            <button class="btn btn-sm btn-outline-primary" @click="$emit('navigate', 'search')">
              <i class="fas fa-search me-2"></i>
              Search Voters
            </button>
            <button class="btn btn-sm btn-outline-primary" @click="$emit('navigate', 'dashboard')">
              <i class="fas fa-chart-bar me-2"></i>
              Dashboard
            </button>
            <div class="ms-md-3">
              <h2 class="mb-1" style="font-size: 1.25rem; font-weight: 600;">
                {{ wardData.ward_no }}
              </h2>
              <p class="text-muted mb-0" style="font-size: 0.875rem;">
                {{ wardData.gram_panchayat }} - {{ wardData.mandal }}
              </p>
            </div>
          </div>
          <div class="text-end">
            <div class="badge bg-primary px-3 py-2" style="font-size: 0.875rem;">
              {{ filteredVoters.length }} / {{ wardData.voters.length }} Voters
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filter Section -->
    <div class="card mb-4">
      <div class="card-body">
        <div class="row g-3">
          <!-- Search Input -->
          <div class="col-12 col-md-6">
            <label class="form-label mb-2" style="font-weight: 500; font-size: 0.875rem;">
              Search by Name or EPIC
            </label>
            <input
              type="text"
              class="form-control ward-search-input"
              placeholder="Enter name or EPIC number..."
              v-model="searchQuery"
            />
          </div>

          <!-- Gender Filter -->
          <div class="col-12 col-md-3">
            <label class="form-label mb-2" style="font-weight: 500; font-size: 0.875rem;">
              Gender
            </label>
            <select class="form-select" v-model="filters.gender">
              <option value="">All</option>
              <option value="M">Male</option>
              <option value="F">Female</option>
              <option value="O">Other</option>
            </select>
          </div>

          <!-- Age Range Filter -->
          <div class="col-12 col-md-3">
            <label class="form-label mb-2" style="font-weight: 500; font-size: 0.875rem;">
              Age Range
            </label>
            <select class="form-select" v-model="filters.ageRange">
              <option value="">All Ages</option>
              <option value="18-30">18 - 30</option>
              <option value="31-45">31 - 45</option>
              <option value="46-60">46 - 60</option>
              <option value="61+">61+</option>
            </select>
          </div>
        </div>

        <!-- Quick Stats -->
        <div class="row g-2 mt-3">
          <div class="col-6 col-md-3">
            <div class="border rounded p-2 text-center" style="background: #f8fafc;">
              <div class="text-primary fw-bold" style="font-size: 1.25rem;">{{ stats.male }}</div>
              <small class="text-muted" style="font-size: 0.75rem;">Male</small>
            </div>
          </div>
          <div class="col-6 col-md-3">
            <div class="border rounded p-2 text-center" style="background: #f8fafc;">
              <div class="text-danger fw-bold" style="font-size: 1.25rem;">{{ stats.female }}</div>
              <small class="text-muted" style="font-size: 0.75rem;">Female</small>
            </div>
          </div>
          <div class="col-6 col-md-3">
            <div class="border rounded p-2 text-center" style="background: #f8fafc;">
              <div class="text-success fw-bold" style="font-size: 1.25rem;">{{ stats.others }}</div>
              <small class="text-muted" style="font-size: 0.75rem;">Others</small>
            </div>
          </div>
          <div class="col-6 col-md-3">
            <div class="border rounded p-2 text-center" style="background: #f8fafc;">
              <div class="text-info fw-bold" style="font-size: 1.25rem;">{{ stats.total }}</div>
              <small class="text-muted" style="font-size: 0.75rem;">Total</small>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Voters List -->
    <div v-if="filteredVoters.length > 0" class="voters-list">
      <div 
        v-for="(voter, index) in filteredVoters" 
        :key="index"
        class="card mb-3"
      >
        <div class="card-body">
          <div class="row align-items-center">
            <div class="col-12 col-md-4">
              <div class="d-flex align-items-center mb-3 mb-md-0">
                <div class="icon-wrapper bg-primary rounded-circle p-2 me-3" style="width: 40px; height: 40px;">
                  <i :class="voter.sex === 'M' ? 'fas fa-mars' : voter.sex === 'F' ? 'fas fa-venus' : 'fas fa-transgender'" class="text-white"></i>
                </div>
                <div class="flex-grow-1">
                  <h5 class="mb-1 fw-semibold" style="font-size: 1rem; color: var(--gray-900);">
                    {{ voter.name }}
                  </h5>
                  <span class="badge bg-secondary" style="font-size: 0.75rem;">{{ voter.serial_no }}</span>
                </div>
                <button 
                  class="btn btn-sm btn-outline-primary preview-btn ms-2" 
                  @click="showVoterDetail(voter)"
                  title="View Full Details"
                >
                  <i class="fas fa-eye me-1"></i>
                  <span class="d-none d-sm-inline">Preview</span>
                </button>
              </div>
            </div>
            <div class="col-12 col-md-8">
              <div class="row g-2">
                <div class="col-6 col-md-3">
                  <small class="text-muted d-block" style="font-size: 0.75rem; font-weight: 500;">Age</small>
                  <strong style="font-size: 0.875rem;">{{ voter.age }} years</strong>
                </div>
                <div class="col-6 col-md-3">
                  <small class="text-muted d-block" style="font-size: 0.75rem; font-weight: 500;">EPIC No.</small>
                  <strong class="text-primary" style="font-size: 0.875rem;">{{ voter.epic_no }}</strong>
                </div>
                <div class="col-6 col-md-3">
                  <small class="text-muted d-block" style="font-size: 0.75rem; font-weight: 500;">Door No.</small>
                  <strong style="font-size: 0.875rem;">{{ voter.door_no || 'N/A' }}</strong>
                </div>
                <div class="col-6 col-md-3">
                  <small class="text-muted d-block" style="font-size: 0.75rem; font-weight: 500;">Relationship</small>
                  <strong style="font-size: 0.875rem;">{{ voter.relationship_type }}: {{ voter.relationship_name }}</strong>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-5">
      <div class="mb-3">
        <i class="fas fa-search fa-4x text-muted opacity-50"></i>
      </div>
      <h5 class="text-muted">No voters found</h5>
      <p class="text-muted">Try adjusting your search or filters</p>
    </div>

    <!-- Voter Detail Modal -->
    <VoterDetail
      v-if="selectedVoter"
      :voter="selectedVoter"
      @close="selectedVoter = null"
    />
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import VoterDetail from './VoterDetail.vue'

export default {
  name: 'WardVoters',
  components: {
    VoterDetail
  },
  props: {
    wardData: {
      type: Object,
      required: true
    }
  },
  emits: ['back', 'navigate'],
  setup(props) {
    const searchQuery = ref('')
    const selectedVoter = ref(null)
    const filters = ref({
      gender: '',
      ageRange: ''
    })

    const showVoterDetail = (voter) => {
      selectedVoter.value = voter
    }

    const filteredVoters = computed(() => {
      let voters = [...props.wardData.voters]

      // Search filter
      if (searchQuery.value.trim()) {
        const query = searchQuery.value.toLowerCase().trim()
        voters = voters.filter(voter => 
          voter.name.toLowerCase().includes(query) ||
          voter.epic_no.toLowerCase().includes(query)
        )
      }

      // Gender filter
      if (filters.value.gender) {
        voters = voters.filter(voter => voter.sex === filters.value.gender)
      }

      // Age range filter
      if (filters.value.ageRange) {
        const range = filters.value.ageRange
        if (range === '18-30') {
          voters = voters.filter(voter => voter.age >= 18 && voter.age <= 30)
        } else if (range === '31-45') {
          voters = voters.filter(voter => voter.age >= 31 && voter.age <= 45)
        } else if (range === '46-60') {
          voters = voters.filter(voter => voter.age >= 46 && voter.age <= 60)
        } else if (range === '61+') {
          voters = voters.filter(voter => voter.age >= 61)
        }
      }

      return voters
    })

    const stats = computed(() => {
      const stats = {
        male: 0,
        female: 0,
        others: 0,
        total: filteredVoters.value.length
      }

      filteredVoters.value.forEach(voter => {
        if (voter.sex === 'M') stats.male++
        else if (voter.sex === 'F') stats.female++
        else stats.others++
      })

      return stats
    })

    return {
      searchQuery,
      filters,
      filteredVoters,
      stats,
      selectedVoter,
      showVoterDetail
    }
  }
}
</script>

<style scoped>
.voters-list .card {
  transition: all 0.2s;
}

.voters-list .card:hover {
  transform: translateX(4px);
  box-shadow: var(--shadow-md);
}

.preview-btn {
  white-space: nowrap;
  border-radius: var(--radius);
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.preview-btn:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.preview-btn:active {
  transform: translateY(0);
}

.icon-wrapper {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ward-search-input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--gray-300);
  border-radius: var(--radius);
  font-size: 0.9375rem;
  transition: var(--transition);
}

.ward-search-input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
  outline: none;
}

.ward-search-input::placeholder {
  color: var(--gray-400);
}

@media (max-width: 768px) {
  .ward-search-input {
    padding: 0.875rem 1rem;
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .ward-search-input {
    font-size: 16px; /* Prevents zoom on iOS */
  }
}

@media (max-width: 768px) {
  .ward-voters .card-body .d-flex {
    flex-direction: column;
    align-items: flex-start !important;
  }

  .ward-voters .btn {
    font-size: 0.875rem;
    padding: 0.5rem 0.75rem;
  }

  .ward-voters .text-end {
    width: 100%;
    text-align: left !important;
    margin-top: 1rem;
  }

  .preview-btn {
    width: 100%;
    margin-top: 0.75rem;
    margin-left: 0 !important;
    justify-content: center;
  }

  .preview-btn span {
    display: inline-block !important;
  }
}
</style>

