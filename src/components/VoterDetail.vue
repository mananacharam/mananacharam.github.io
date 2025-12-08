<template>
  <div class="voter-detail-overlay" @click.self="close">
    <div class="voter-detail-card">
      <div class="card shadow-lg">
        <div class="card-header bg-primary text-white border-0">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h4 class="mb-1 text-white" style="font-size: 1.25rem; font-weight: 600;">{{ voter.name }}</h4>
              <small class="text-white-50" style="font-size: 0.875rem;">{{ voter.ward }}</small>
            </div>
            <button class="btn btn-link text-white p-0" @click="close" style="text-decoration: none;">
              <i class="fas fa-times"></i>
            </button>
          </div>
        </div>
        
        <div class="card-body">
          <div class="row g-4">
            <!-- Personal Information -->
            <div class="col-12">
              <h5 class="mb-3" style="font-size: 1rem; font-weight: 600; color: var(--gray-700);">
                Personal Information
              </h5>
              <div class="row g-3">
                <div class="col-12 col-md-6">
                  <div class="detail-item">
                    <label class="detail-label">Serial Number</label>
                    <div class="detail-value">{{ voter.serial_no }}</div>
                  </div>
                </div>
                <div class="col-12 col-md-6">
                  <div class="detail-item">
                    <label class="detail-label">Age & Gender</label>
                    <div class="detail-value">
                      {{ voter.age }} years, 
                      <span :class="voter.sex === 'M' ? 'text-primary' : voter.sex === 'F' ? 'text-danger' : 'text-success'">
                        {{ voter.sex === 'M' ? 'Male' : voter.sex === 'F' ? 'Female' : 'Other' }}
                      </span>
                    </div>
                  </div>
                </div>
                <div class="col-12 col-md-6">
                  <div class="detail-item">
                    <label class="detail-label">EPIC Number</label>
                    <div class="detail-value text-primary fw-semibold">{{ voter.epic_no }}</div>
                  </div>
                </div>
                <div class="col-12 col-md-6">
                  <div class="detail-item">
                    <label class="detail-label">Door Number</label>
                    <div class="detail-value">{{ voter.door_no || 'N/A' }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Relationship Information -->
            <div class="col-12">
              <h5 class="mb-3" style="font-size: 1rem; font-weight: 600; color: var(--gray-700);">
                Relationship Information
              </h5>
              <div class="row g-3">
                <div class="col-12 col-md-6">
                  <div class="detail-item">
                    <label class="detail-label">Relationship Type</label>
                    <div class="detail-value">{{ voter.relationship_type }}</div>
                  </div>
                </div>
                <div class="col-12 col-md-6">
                  <div class="detail-item">
                    <label class="detail-label">Relationship Name</label>
                    <div class="detail-value fw-semibold">{{ voter.relationship_name }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Electoral Information -->
            <div class="col-12">
              <h5 class="mb-3" style="font-size: 1rem; font-weight: 600; color: var(--gray-700);">
                Electoral Information
              </h5>
              <div class="row g-3">
                <div class="col-12 col-md-4">
                  <div class="detail-item">
                    <label class="detail-label">Assembly Constituency (A.C No.)</label>
                    <div class="detail-value">{{ voter.ac_no }}</div>
                  </div>
                </div>
                <div class="col-12 col-md-4">
                  <div class="detail-item">
                    <label class="detail-label">Polling Station (PS No.)</label>
                    <div class="detail-value">{{ voter.ps_no }}</div>
                  </div>
                </div>
                <div class="col-12 col-md-4">
                  <div class="detail-item">
                    <label class="detail-label">Serial List (SL No.)</label>
                    <div class="detail-value">{{ voter.sl_no }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="card-footer bg-light border-0">
          <div class="d-flex justify-content-end">
            <button class="btn btn-primary" @click="close">
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VoterDetail',
  props: {
    voter: {
      type: Object,
      required: true
    }
  },
  emits: ['close'],
  setup(props, { emit }) {
    const close = () => {
      emit('close')
    }

    return {
      close
    }
  }
}
</script>

<style scoped>
.voter-detail-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  z-index: 1050;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  animation: fadeIn 0.2s ease-out;
}

.voter-detail-card {
  width: 100%;
  max-width: 900px;
  max-height: 90vh;
  overflow-y: auto;
  animation: slideUp 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.card {
  border-radius: var(--radius-lg);
}

.card-header {
  border-radius: var(--radius-lg) var(--radius-lg) 0 0 !important;
}

.detail-item {
  background: var(--gray-50);
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  padding: 0.875rem 1rem;
}

.detail-label {
  display: block;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--gray-500);
  margin-bottom: 0.5rem;
}

.detail-value {
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--gray-900);
}

.icon-wrapper {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 768px) {
  .voter-detail-card {
    max-width: 100%;
    max-height: 100vh;
  }
  
  .card-body {
    padding: 1.5rem !important;
  }
}
</style>

