# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Jinja templates."""

import jinja2

import pkg_resources

PACKAGE = 'cbmc_viewer'
TEMPLATES = 'templates'

SUMMARY_TEMPLATE = 'summary.jinja.html'
CODE_TEMPLATE = 'code.jinja.html'
TRACE_TEMPLATE = 'trace.jinja.html'

# runtime analysis metrics
ALIAS_SUMMARY_TEMPLATE = 'alias.jinja.html'
ARRAY_CONSTRAINT_SUMMARY_TEMPLATE = 'array.jinja.html'
BYTEOP_SUMMARY_TEMPLATE = 'byteop.jinja.html'
CLAUSE_SUMMARY_TEMPLATE = 'clause.jinja.html'
MEMOP_SUMMARY_TEMPLATE = 'memop.jinja.html'
RUNTIME_ANALYSIS_SUMMARY_TEMPLATE = 'runtime_analysis_report.jinja.html'

ENV = None

def env():
    """The jinja environment."""

    # pylint: disable=global-statement
    global ENV

    if ENV is None:
        template_dir = pkg_resources.resource_filename(PACKAGE, TEMPLATES)
        ENV = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir)
        )
    return ENV

def render_summary(summary):
    """Render summary as html."""

    return env().get_template(SUMMARY_TEMPLATE).render(
        summary=summary
    )

def render_code(filename, path_to_root, lines):
    """Render annotated source code as html."""

    return env().get_template(CODE_TEMPLATE).render(
        filename=filename, path_to_root=path_to_root, lines=lines
    )

def render_trace(name, desc, srcloc, steps):
    """Render annotated trace as html."""

    return env().get_template(TRACE_TEMPLATE).render(
        prop_name=name, prop_desc=desc, prop_srcloc=srcloc, steps=steps
    )

def render_alias_summary(alias_summary):
    """Render points-to set metrics as html."""

    return env().get_template(ALIAS_SUMMARY_TEMPLATE).render(
        summary=alias_summary.summary, max=alias_summary.max, 
        total=alias_summary.total
    )

def render_array_constraint_summary(array_constraint_summary):
    """Render array constraint summary as html."""

    return env().get_template(ARRAY_CONSTRAINT_SUMMARY_TEMPLATE).render(
        summary=array_constraint_summary
    )

def render_byteop_summary(byteop_summary):
    """Render byte op metrics as html."""

    return env().get_template(BYTEOP_SUMMARY_TEMPLATE).render(
        byteops=byteop_summary
    )

def render_clause_summary(clause_summary, core_instr, loc_not_in_core):
    """Render solver query complexity metric as html."""

    return env().get_template(CLAUSE_SUMMARY_TEMPLATE).render(
        summary=clause_summary, core=core_instr, notcore=loc_not_in_core
    )

def render_memop_summary(memop_summary):

    return env().get_template(MEMOP_SUMMARY_TEMPLATE).render(
        summary=memop_summary
    )

def render_runtime_analysis_summary(runtime_analysis_summary):
    """Render runtime analysis summary as html."""

    return env().get_template(RUNTIME_ANALYSIS_SUMMARY_TEMPLATE).render(
        summary=runtime_analysis_summary
    )
