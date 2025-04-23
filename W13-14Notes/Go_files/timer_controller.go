/*
Copyright 2025.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package controller

import (
	"context"
	"time"

	"k8s.io/apimachinery/pkg/runtime"
	ctrl "sigs.k8s.io/controller-runtime"
	"sigs.k8s.io/controller-runtime/pkg/client"
	"sigs.k8s.io/controller-runtime/pkg/log"

	timerv1 "github.com/randybrown12/timer-operator/api/v1"
)

// TimerReconciler reconciles a Timer object
type TimerReconciler struct {
	client.Client
	Scheme *runtime.Scheme
}

// +kubebuilder:rbac:groups=timer.uco.edu,resources=timers,verbs=get;list;watch;create;update;patch;delete
// +kubebuilder:rbac:groups=timer.uco.edu,resources=timers/status,verbs=get;update;patch
// +kubebuilder:rbac:groups=timer.uco.edu,resources=timers/finalizers,verbs=update

// Reconcile is part of the main kubernetes reconciliation loop which aims to
// move the current state of the cluster closer to the desired state.
// TODO(user): Modify the Reconcile function to compare the state specified by
// the Timer object against the actual cluster state, and then
// perform operations to make the cluster state reflect the state specified by
// the user.
//
// For more details, check Reconcile and its Result here:
// - https://pkg.go.dev/sigs.k8s.io/controller-runtime@v0.19.0/pkg/reconcile
func (r *TimerReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
	logger := log.FromContext(ctx)

	// TODO(user): your logic here
	timer := &timerv1.Timer{}
	err := r.Get(ctx, req.NamespacedName, timer)

	if err != nil {
		logger.Error(err, "Failed to get Timer", "NamespacedName", req.NamespacedName)
		return ctrl.Result{}, client.IgnoreNotFound(err)
	}

	duration, err := time.ParseDuration(timer.Spec.Duration)
	if err != nil {
		logger.Error(err, "Failed to parse duration", "Duration", timer.Spec.Duration)
		return ctrl.Result{}, err
	}

	if timer.Status.State == "" {
		timer.Status.State = "Running"

		err := r.Status().Update(ctx, timer)
		if err != nil {
			logger.Error(err, "Failed to update Timer status", "Timer", timer)
			return ctrl.Result{}, err
		}

		logger.Info("Starting Timer", "Timer", timer)
		return ctrl.Result{RequeueAfter: duration}, nil
	}

	if timer.Status.State == "Running" {
		timer.Status.State = "Completed"

		err = r.Status().Update(ctx, timer)
		if err != nil {
			logger.Error(err, "Failed to update Timer status", "Timer", timer)
			return ctrl.Result{}, err
		}
		logger.Info("Timer completed for "+timer.Spec.Duration+"\nMessage: "+timer.Spec.Message, "Timer", timer)
	}

	return ctrl.Result{}, nil
}

// SetupWithManager sets up the controller with the Manager.
func (r *TimerReconciler) SetupWithManager(mgr ctrl.Manager) error {
	return ctrl.NewControllerManagedBy(mgr).
		For(&timerv1.Timer{}).
		Complete(r)
}
